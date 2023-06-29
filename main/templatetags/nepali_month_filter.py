from django import template


register = template.Library()

MONTH_NAMES_NP = {
    '01': 'बैशाख',
    '02': 'जेठ',
    '03': 'असार',
    '04': 'श्रावण',
    '05': 'भदौ',
    '06': 'आश्विन',
    '07': 'कार्तिक',
    '08': 'मंसिर',
    '09': 'पुष',
    '10': 'माघ',
    '11': 'फाल्गुन',
    '12': 'चैत्र',
}

@register.filter
def nepali_month_name(month_number):
    return MONTH_NAMES_NP.get(month_number, '')