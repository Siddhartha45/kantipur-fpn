"""for selecting user roles"""
ROLE_CHOICES = (
    ('A', 'Admin'),
    ('V', 'Verifier'),
    ('DE', 'Data Entry'),
)

"""for selecting users department"""
DEPARTMENT_CHOICES = (
    ('IE', 'Import/Export'),
    ('DO', 'Division Office'),
    ('FO', 'Food Office'),
    ('FFSQRD', 'FFSQRD'),
    ('FTDND', 'FTDND'),
    ('NFFRL', 'NFFRL'),
    ('A', 'Account'),
)

"""for selecting users form types"""
FORM_TYPES = (
    ('Account', 'Account'),
    ('Report', 'Report'),
)