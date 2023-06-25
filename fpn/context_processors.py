import nepali_datetime

def current_nepali_date(request):
    return {
        'current_nepali_date': nepali_datetime.date.today().strftime("%Y/%m/%d"),
        'current_nepali_year': nepali_datetime.date.today().strftime("%Y"),
        'current_nepali_month': nepali_datetime.date.today().strftime("%B"),
    }