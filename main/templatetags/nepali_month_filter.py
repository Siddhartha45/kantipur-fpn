from django import template


register = template.Library()

MONTH_NAMES_NP = {
    '01': 'Baishakh',
    '02': 'Jestha',
    '03': 'Asar',
    '04': 'Shrawan',
    '05': 'Bhadra',
    '06': 'Ashoj',
    '07': 'Kartik',
    '08': 'Mangsir',
    '09': 'Poush',
    '10': 'Magh',
    '11': 'Falgun',
    '12': 'Chaitra',
}

@register.filter
def nepali_month_name(month_number):
    return MONTH_NAMES_NP.get(month_number, '')