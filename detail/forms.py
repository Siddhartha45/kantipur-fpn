from django.forms import ModelForm
from .models import SiteSettings


class SiteSettingsModelForm(ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'