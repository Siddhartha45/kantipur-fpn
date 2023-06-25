def normalize_email(email):
        """customizing the normalize_email function to turn email_name and domain_name to lowercase"""
        
        email = email
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email_name = email_name.lower()
            domain_part = domain_part.lower()
            email = '@'.join([email_name, domain_part])
        return email
