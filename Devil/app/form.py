from django import forms
from app.models import *



class Admin_Reg(forms.ModelForm):
    class Meta:

        model = User
        fields=['first_name','last_name','email','username','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}


class Upload(forms.ModelForm):

    class Meta:

        model = Movies
        fields = '__all__'