from django import forms
from item.models import item

class ItemPostForm(forms.Form):
    item_name=forms.CharField()
    category=forms.CharField()
    price_expected=forms.IntegerField()
    old=forms.IntegerField()
    description=forms.CharField(widget=forms.Textarea)
    item_image=forms.ImageField()

