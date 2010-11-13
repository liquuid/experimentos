from library.models import Track
from django import forms
 
class TrackForm(forms.Form):
    url = forms.CharField()
    class Meta:
        model = Track
