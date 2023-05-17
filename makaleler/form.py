from django import forms

from makaleler.models import makale
class article1(forms.ModelForm):
    class Meta:
        model=makale
        fields=["title","content"]
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }