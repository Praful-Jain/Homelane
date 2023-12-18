from django.db.models import F
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from .models import User, BackboneCustomerEvent

supplier_id = 101    
class HomeView(View):
    template_name = 'homelane.html'  
    per_page = 10   # number of records to be rendered per page
    
    # Django's ORM uses 'lazy loading' feature, this means that the actual database query is executed only when the data is needed.
    def getCustomerList(self, name, apt_type, stage):
        backbone_customer_events = BackboneCustomerEvent.objects.filter(showroom_id__supplier_id=supplier_id)   # From BackboneCustomerEvent filter the records having supplier_id=vendor_id
        cust_ids_for_vendor = backbone_customer_events.values_list('cust_id', flat=True)    #  Get cust_ids associated with this vendor
        #  Fetch the profile and info of customers with these cust_ids
        customers_info_list = User.objects.filter(user_id__in=cust_ids_for_vendor)          

        # Forming a QuerySet using Django's annotate and F expressions - 
        # F object in Django is used to refer to a model field within a query and perform operations without having to pull data into Python memory. ie..The F object is particularly useful when you want to perform updates or comparisons between fields on the database side.
        customers_info_list = customers_info_list.annotate(
            name=F('customer_profile_id__name'),
            appointment_type=F('user_id__appointment_type'),
            appointment_time=F('user_id__appointment_time'),
            stage=F('user_id__stage'),
        )
        
        # Filtering
        # The filtering is done before annotating to avoid overwriting the queryset
        if name:
            customers_info_list = customers_info_list.filter(customer_profile_id__name__icontains=name)  # __icontains, __iexact lookups
        if apt_type:
            customers_info_list = customers_info_list.filter(user_id__appointment_type=apt_type)
        if stage:
            customers_info_list = customers_info_list.filter(user_id__stage=stage)
        return customers_info_list
        
    def get(self, request, *args, **kwargs):
        name, apt_type, stage = (request.GET.get(key, '') for key in ['name', 'apt_type', 'stage'])
        
        customer_info_list = self.getCustomerList(name, apt_type, stage)    #  customer_info_list queryset is a representation of the SQL query that will be executed when the data is requested.
        
        paginator = Paginator(customer_info_list, self.per_page)        # Paginator class object, the paginator doesn't immediately fetch all records from the database. 
        page_number = request.GET.get('page',1)         
        # Paginator only fetches the subset of records needed for the current page. 
        page_object = paginator.get_page(page_number)   # Page object     # get_page() method will handle outofbound and datatype errors  
        
        return render(request, self.template_name, {'customer_info_list':page_object, 'name':name, 'apt_type':apt_type, 'stage':stage, })

    











# <a href="?page={{ customer_info_list.previous_page_number }}">Previous</a>
# Using "?page={{ customer_info_list.previous_page_number }}" in the href attribute is a valid way to 
# include the page parameter as a query parameter in the URL.

# In the redirect function in Django, the reverse function is used internally to generate URLs based on view names.
# The reverse function, by default, generates URLs with path parameters (e.g., /some_path/1/) rather than query parameters (e.g., /some_path/?page=1)
# return redirect(f'home_view/?page={page_number}')         eg. url = "/2" not "/?page=2"





# Instead of generating a list we can also form a QuerySet using Django's annotate and F expressions.
# annotated_customers = customers_info_list.annotate(
#         name=F('customer_profile_id__name'),
#         appointment_type=F('user_id__appointment_type'),
#         appointment_time=F('user_id__appointment_time'),
#         stage=F('user_id__stage'),
#         index=Value(1, output_field=IntegerField()),  # You can replace this with the desired index
#     )

# When you pass a serialized queryset (or any data) to a template, it becomes plain data
    
