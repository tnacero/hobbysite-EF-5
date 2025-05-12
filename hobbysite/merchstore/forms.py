"""
Importing forms from Django with Recipe models for the forms.
"""
from django import forms
from .models import Product, Transaction

class ProductForm(forms.ModelForm) :
    """Class for the ProductForm form."""
    class Meta:
        """Meta class for the fields utilized by ProductForm."""
        model = Product
        fields = "__all__"
        widgets = {
            "product_type":forms.Select()
            ,"status":forms.Select(),
            
        }

class TransactionForm(forms.ModelForm) :
    """
    Class for the TransactionForm form.
    """
    class Meta:
        """Meta class for the fields utilized by Transaction"""
        model = Transaction
        fields = ['product', 'amount', 'status']
