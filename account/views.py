from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q


from .forms import RegistrationForm
from .token import account_activation_token
from .models import UserBase


@login_required
def dashboard(request):
    return render(request,
                  'account/user/dashboard.html',
                  {'section': 'profile'})


def account_register(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.email = registration_form.cleaned_data['email']
            user.set_password(registration_form.cleaned_data['password'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(subject, message, 'blogtestsmtp@ukr.net',
                      [user.email], fail_silently=False)
            messages.success(request, "Реєстрація успішна. Буль ласка, перевірте Вашу поштову скриню для активації.")
            return redirect('/')
    else:
        registration_form = RegistrationForm()
    return render(request, 'account/registration.html', {'form': registration_form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Ви успішно авторизувалися!")
        return redirect('/')

    else:
        return render(request, 'account/activation_invalid.html')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = UserBase.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "account/user/password_reset_email.html"
                    current_site = get_current_site(request)
                    c = {
                        "email": user.email,
                        'domain': current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'blogtestsmtp@ukr.net', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset_email_confirm/")
    password_reset_form = PasswordResetForm()
    return render(request=request,
                  template_name="account/user/password_reset_form.html",
                  context={"password_reset_form":password_reset_form})
