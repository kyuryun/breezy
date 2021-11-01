from django import forms
from home.models import MyUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호  ', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'최소 6자~최대 16자로 입력해주세요.'}))
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'비밀번호를 다시 입력해주세요.'}))

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'email', 'phone']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'15자 이내로 입력해주세요.'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'01000000000'}),
        }
        labels = {
            'username':'아이디 ',
            'Password':'비밀번호',
            'email':'이메일',
            'phone':'전화번호'
        }

        def clean_password(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
            else:
                return cd['password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

class FindIdForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'email', )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


