from django import forms

from operation.models import userAsk

class UserAskForm(forms.ModelForm):
    class Meta:
        model = userAsk
        fields = ['name','telphone','coure_name']

    #电话号码验证
    # def clean_mobile(self):
    #     mobile = self

