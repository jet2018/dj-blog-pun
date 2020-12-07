from .models import Gallery
from django.forms import ModelForm, Textarea, CharField


class galleryForm(ModelForm):

    class Meta:
        model = Gallery
        fields = ['Image', 'short_description']
        widgets = {
            'short_description': Textarea(attrs={
                    'rows':3, 'style':'resize:none;',
                    'placeholder':'Write anything special about your hostel',
            }),
        }
