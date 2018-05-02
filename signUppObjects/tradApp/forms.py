from django import forms
from .models import Coach_Orders
class CoachOrdersForm(forms.ModelForm):
    class Meta:
        model = Coach_Orders
        fields = ['username','order_sn','coach_name','pay_mount','order_mount','pay_type']

