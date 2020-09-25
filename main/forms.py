from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ContactForm(forms.Form):
    CATEGORIES = [
    ('1', 'アプリに関するお問い合わせ'),
    ('2', '採用に関するお問い合わせ'),
    ('3', 'その他')
    ]
    name = forms.CharField(label='名前', max_length=50)
    email = forms.EmailField(label='メールアドレス', required=False, help_text='※任意')
    text = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)
    category = forms.ChoiceField(label='お問い合わせ種別', choices=CATEGORIES)

    def clean(self):
        category = self.cleaned_data.get('category')
        email = self.cleaned_data.get('email')
        if category == '2' and not email:
            self.add_error(None, '採用に関するお問い合わせの場合メールアドレスは必須です。')
        return self.cleaned_data

