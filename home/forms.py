from django import forms

class LoginForms(forms.Form):
    login_user = forms.CharField(
        label='Usuario', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite seu usuario'
            }
        )
    )

    login_password = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }
        )
    )
