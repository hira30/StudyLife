from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import SignUpForm, ContactForm
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = 'main/index.html'


class UserOnlyMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class MypageView(LoginRequiredMixin, UserOnlyMixin, TemplateView):
    template_name = 'main/mypage.html'


class ProfileChangeView(LoginRequiredMixin, UserOnlyMixin, UpdateView):
    template_name = 'main/profile_change.html'
    model = User
    fields = ('username', 'email')
    success_url = reverse_lazy('main:mypage')


def signup(request):
    signup_form = SignUpForm(request.POST or None)
    if request.method == "POST" and signup_form.is_valid():
        user = signup_form.save()
        input_username = signup_form.cleaned_data['username']
        input_password = signup_form.cleaned_data['password1']
        user = authenticate(username=input_username, password=input_password)
        login(request, user)
        return redirect('studyapp:list')
    context = {
          "signup_form": signup_form,
    }
    return render(request, 'main/signup.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = 'ユーザー：' + form.cleaned_data['name'] + ' からのお問い合わせ'   # 件名
            text = 'お問い合わせ内容：'+ '\n' + form.cleaned_data['text']    # 本文
            from_email = form.cleaned_data['email']  # 送信先
            recipients = [settings.EMAIL_HOST_USER]  # 宛先リスト
            recipients.append(from_email)
            try:
                send_mail(subject, text, from_email, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('main:complete')

    else:
        form = ContactForm()

    context = {'form':form}
    return render(request, 'main/contact.html', context)


def contact_complete(request):
    return render(request, 'main/contact_complete.html')
