from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['english', 'turkish']
        widgets = {
            'english': forms.TextInput(attrs={'placeholder': 'İngilizce Kelime'}),
            'turkish': forms.TextInput(attrs={'placeholder': 'Türkçe Karşılığı'}),
        }