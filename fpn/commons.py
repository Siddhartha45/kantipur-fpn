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

"""for selecting offices"""
OFFICE_CHOICES = (
    ('IE', 'Import/Export'),
    ('DO', 'Division Office'),
    ('FO', 'Food Office'),
)

"""choices for anugaman views"""
ANUGAMAN_CHOICES = (
    ('udyog', 'udyog'),
    ('pasal', 'pasal'),
    ('supermarket', 'supermarket'),
    ('godam', 'godam'),
    ('hotel', 'hotel'),
    ('dana', 'dana'),
    ('anya', 'anya'),
)

"""choices for namuna bisleysan"""
NAMUNA_BISLEYSAN_CHOICES = (
    ('milk', 'milk'),
    ('oil', 'oil'),
    ('fruits', 'fruits'),
    ('spice', 'spice'),
    ('tea', 'tea'),
    ('salt', 'salt'),
    ('khadanna', 'khadanna'),
    ('water', 'water'),
    ('sweets', 'sweets'),
    ('confectionery', 'confectionery'),
    ('meat', 'meat'),
    ('others', 'others'),
    ('grain', 'grain'),
)

"""choices for ekai fields in BisleysanBibaran models"""
EKAI_CHOICES = (
    ('S', 'संख्या'),
    ('P', 'पटक'),
)