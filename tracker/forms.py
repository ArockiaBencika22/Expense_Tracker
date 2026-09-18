from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields=['Title', 'Amount', 'Category', 'Transaction_type', 'Date']
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'Category': forms.Select(attrs={'class': 'form-control'}),
            'Transaction_type': forms.Select(attrs={'class': 'form-control'}),
        }

