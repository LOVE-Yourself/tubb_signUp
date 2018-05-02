from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile
class LoginForm(forms.Form):
    username = forms.RegexField(regex='^1[356789]\d{9}$',error_messages={'required':u'手机号不能为空','invalid':u'手机号格式不正确'})
    password = forms.CharField(min_length=6,error_messages={'required':u'密码不能为空','invalid':u'密码设置过短'})
    captcha = CaptchaField(error_messages={'required':u'验证码不能为空','invalid': u'验证码出错'})


class RegisterForm(forms.Form):
    username = forms.RegexField(regex='^1[356789]\d{9}$',error_messages={'required':u'手机号不能为空','invalid':u'手机号格式不正确'})
    password1 = forms.CharField(min_length=6, error_messages={'required': u'密码不能为空', 'invalid': u'密码设置过短'})
    password2 = forms.CharField(min_length=6, error_messages={'required': u'密码不能为空', 'invalid': u'密码设置过短'})
    verifyNum = forms.CharField(error_messages = {'invalid':u'验证码出错'})

class ForgetForm(forms.Form):
    username = forms.RegexField(regex='^1[356789]\d{9}$',error_messages={'required':u'手机号不能为空','invalid':u'手机号格式不正确'})
    password1 = forms.CharField(min_length=6, error_messages={'required': u'密码不能为空', 'invalid': u'密码设置过短'})
    password2 = forms.CharField(min_length=6, error_messages={'required': u'密码不能为空', 'invalid': u'密码设置过短'})
    verifyNum = forms.CharField(error_messages = {'invalid':u'验证码出错'})

class ChangeForm(forms.Form):
    password = forms.CharField(required=True,min_length=6)
    password2 = forms.CharField(required=True,min_length=6)

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']