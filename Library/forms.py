from django import forms
from django.contrib.auth.models import User
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class issueform(forms.ModelForm):
    class Meta:
        model = IssueBook
        fields = '__all__'

        widgets = {
            'stud_enroll_no':forms.TextInput(attrs={'class':'form-control'}),
            'stud_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'book_id': forms.TextInput(attrs={'class': 'form-control'}),

            # 'issue_date': DateInput(attrs={'type': 'date'}),
             'return_date': DateInput(attrs={'type': 'date'}),
            # 'return_date': forms.DateTimeField(attrs={'class': 'form-control'}),
       }

class addform(forms.ModelForm):
    class Meta:
        model = AddBooks
        fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book_id': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }

class returnform(forms.ModelForm):
    class Meta:
        model = Returnbook
        fields = '__all__'
        widgets = {
            'stud_enroll_no': forms.TextInput(attrs={'class': 'form-control'}),
            'stud_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'book_id': forms.TextInput(attrs={'class': 'form-control'}),
             'return_date': DateInput(attrs={'type': 'date'}),
        }

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

