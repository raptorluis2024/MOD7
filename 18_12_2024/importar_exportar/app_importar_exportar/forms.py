from django import forms

class ExcelForm(forms.Form):
    excel_file = forms.FileField()