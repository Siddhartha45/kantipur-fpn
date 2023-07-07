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

"""choices for anugamanbibaran model"""
ANUGAMAN_CHOICES = (
    ('udyog', 'उद्योग'),
    ('pasal', 'पसल'),
    ('supermarket', 'सुपरमार्केट'),
    ('godam', 'गोदाम'),
    ('hotel', 'होटल, रेस्टुरेन्ट, मिठाई पसल आदी'),
    ('dana', 'दाना पदार्थ'),
    ('anya', 'अन्य'),
)

"""choices for namunabisleysan, aayatniryat and prayogsalabisleysan models"""
TYPES_CHOICES = (
    ('milk', 'दुध तथा दुध पदार्थ'),
    ('oil', 'तेल तथा घिउ जन्य'),
    ('fruits', 'फल तथा सागपात'),
    ('spice', 'मसला'),
    ('tea', 'चिया, कफि'),
    ('salt', 'नुन'),
    ('khadanna', 'खाद्यान्न दलहन र सोवाट बनेका'),
    ('water', 'प्र. पिउने पानी'),
    ('sweets', 'गुलियो पदार्थ'),
    ('confectionery', 'कन्फेक्सनरी'),
    ('meat', 'मासु तथा मासुजन्य'),
    ('grain', 'दाना'),
    ('others', 'अन्य'),
)

"""choices for ekai fields in BisleysanBibaran model"""
EKAI_CHOICES = (
    ('S', 'संख्या'),
    ('P', 'पटक'),
)

"""choices for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण model"""
LOGO_CHOICES = (
    ('green', 'हरियो स्टिकर'),
    ('yellow1', 'पेहेलोमा एउटा रातो धर्सो'),
    ('yellow2', 'पेहेलोमा दुइटा रातो धर्सो'),
    ('red', 'रातो स्टिकर'),
)

"""choices for DetailAnugaman model"""
DETAIL_ANUGAMAN_CHOICES = (
    ('B', 'बजार/पसल'),
    ('K', 'खाद्य उद्योग'),
    ('H', 'होटल, रेष्टुरेण्ट, मिठाई पसल'),
    ('S', 'संयुक्त अनुगमन'),
    ('D', 'दाना उद्योग'),
    ('A', 'अन्य'),
)

"""choices for logo in DetailHotel model"""
DETAIL_LOGO_CHOICES = (
    ('A', 'अति उत्तम'),
    ('B', 'उत्तम'),
    ('C', 'संतोषजनक'),
    ('D', 'सामान्य'),
    ('E', 'स्तरकिरणमा नपरेको'),
)

"""choices for samuha in DetailRegistration model"""
DETAIL_SAMUHA_CHOICES = (
    ('A', 'दूध तथा दुग्ध पदार्थहरु'),
    ('B', 'तेल तथा घउि'),
    ('C', 'फल तथा सागपात पदार्थहरु'),
    ('D', 'मसला पदार्थहरु'),
    ('E', 'चिया, कफि कोका तथा सो बाट बनेका पदार्थहरु'),
    ('F', 'नुन'),
    ('G', 'खाद्यान्न दलहन तथा सो बाट बनेका पदार्थहरु'),
    ('H', 'प्याक गरएिको पउिने पानी'),
    ('I', 'गुलियो पदार्थ'),
    ('J', 'कन्फेक्सनरी'),
    ('K', 'आहारपुरक'),
    ('L', 'ईनर्जी ड्रिंक'),
    ('M', 'बालआहार'),
    ('N', 'विविध')
)

"""choices for srot in DetailGunaso model"""
DETAIL_SROT_CHOICES = (
    ('A', 'गुनासो पेटीका'),
    ('B', 'गुनासो अधिकारी समक्ष'),
    ('C', 'जिल्ला प्रशासन कार्यालयबाट लेखिआएको'),
    ('D', 'बाणिज्य कार्यालयबाट लेखिआएको'),
    ('E', 'पत्र पत्रिका'),
    ('F', 'अख्तियार दु. अ.आ.'),
    ('G', 'पत्रकार'),
    ('H', 'हेलो सरकार'),
    ('I', 'उपभोक्ता संघ संस्था'),
    ('J', 'अन्य'),
)

"""choices for selecting months in  PragatiBibaran"""
MONTHS_CHOICES = (
    ('A', 'वैशाख'),
    ('B', 'जेठ'),
    ('C', 'असार'),
    ('D', 'साउन'),
    ('E', 'भदौ'),
    ('F', 'असोज'),
    ('G', 'कार्तिक'),
    ('H', 'मंसिर'),
    ('I', 'पुष'),
    ('J', 'माघ'),
    ('K', 'फागुन'),
    ('L', 'चैत'),
)

"""choices for selecting kharcha type in  PragatiBibaran"""
KHARCHA_CHOICES = (
    ('P', 'पुँजीगत'),
    ('C', 'चालु'),
)


FORM_STATUS_CHOICES = (
    ('ok', 'ok'),
    ('pending', 'pending'),
)