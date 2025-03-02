from django import forms
from .models import Fanlar,Student

class StudentForm(forms.Form):
    fullname = forms.CharField(max_length=150,
        label='Sarlavha kiriting ',
        widget=forms.TextInput(attrs={"class":'form-control'}))
    phone = forms.RegexField(regex=r'^\+998\d{9}$',
        label="Telefon raqam",
        error_messages={"invalid": "Telefon raqamni +998XXXXXXXXX formatida kiriting"},
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "+998901234567"}))
    location = forms.CharField(label="Manzil",
    widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Manzilingizni kiriting..."}))
    fan = forms.ModelChoiceField(empty_label='Kategoriyani tanlang',
        label='Kategoriya',queryset=Fanlar.objects.all(),
        widget=forms.Select(attrs={"class":'form-control'}))
class FanlarForm(forms.Form):
    model = Fanlar
    title = forms.CharField(max_length=140,label='Sarlavha kiriting ',
                                widget=forms.TextInput(attrs={"class":'form-control'}))

