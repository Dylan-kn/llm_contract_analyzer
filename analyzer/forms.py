from django import forms 
from .models import Contract

class ContractUploadForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['file']

class QuestionForm(forms.Form):
    question = forms.CharField(
        label = 'Ask a question about this contract',
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. When does this contract expire?'})
    )