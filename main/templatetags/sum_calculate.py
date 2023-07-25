from django import template
from main.report_sum import office_namunabibaran_monthly_sum

register = template.Library()

@register.filter
def calculate_sum(request, office_id, month):
    return office_namunabibaran_monthly_sum(request, office_id, month)