# forms.py
from django import forms
from .models import Gradepoints, Branchcodes

class GradepointForm(forms.ModelForm):
    class Meta:
        model = Gradepoints
        fields = ['Grade', 'Points', 'Status', 'Presence']

class BranchcodeForm(forms.ModelForm):
    class Meta:
        model = Branchcodes
        fields = ['Branch', 'Code', 'Abbrevation']
