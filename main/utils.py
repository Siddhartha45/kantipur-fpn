from detail.models import SiteSettings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


def is_form_open():
    """Checks if the form filled date is between open and close dates"""
    
    try:
        obj = SiteSettings.objects.order_by('-id').first()  #fetches the latest obj by id 
        open_date = obj.open_date
        close_date = obj.close_date
    except ObjectDoesNotExist:
        # Handle the case where obj does not exists
        obj = None
    except AttributeError:
        # Handle the case where obj exists, but open_date or close_date is not available
        open_date = None
        close_date = None
    
    current_date = datetime.now().date()
    
    return open_date <= current_date <= close_date 