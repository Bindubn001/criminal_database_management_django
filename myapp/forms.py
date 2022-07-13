from django.forms import ModelForm
from .models import Crime,Prison,Criminal,Victim,Trial
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CrimeForm(ModelForm):
    class Meta:
        model = Crime
        fields = '__all__'

class PrisonForm(ModelForm):
    class Meta:
        model = Prison
        fields = '__all__'

class CriminalForm(ModelForm):
    class Meta:
        model = Criminal
        fields = '__all__'

class TrialForm(ModelForm):
    class Meta:
        model = Trial
        fields = '__all__'

class VictimForm(ModelForm):
    class Meta:
        model = Victim
        fields = '__all__'

class CreateUserForm(UserCreationForm):
     class Meta:
        model=User
        fields = ['username','email','password1','password2']