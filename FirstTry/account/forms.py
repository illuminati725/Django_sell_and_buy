from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from account.models import UserInfo


class UserRegisterForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email', 'password' )


class ProfileCompleteForm(forms.ModelForm):
    #
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    # gender = forms.CharField()
    # city = forms.CharField()
    # country = forms.CharField()
    # address = forms.CharField()
    # phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),
    #                                   required=True)
    # profile_pic = forms.ImageField()

    class Meta:
        model=UserInfo

        fields=('gender','city','country','address','phone_number','profile_pic')
