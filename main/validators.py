from django.core.exceptions import ValidationError
import re


def validate_nepali_date(value):
    """validators to check that only valid dates are saved in database"""
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    if not pattern.match(value):
        raise ValidationError('Invalid Nepali date format. Use YYYY-MM-DD format.')