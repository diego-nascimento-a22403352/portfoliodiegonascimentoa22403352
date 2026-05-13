from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

# View de Registo
def registo_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Adiciona automaticamente ao grupo autores
            grupo_autores, created = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo_autores)
            
            # Faz login automático
            login(request, user)
            return redirect('projetos')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registo.html', {'form': form})

# View de Login normal (Password)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('projetos')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# View de Logout
def logout_view(request):
    logout(request)
    return redirect('projetos')

# View para pedir o Link Mágico (Formulário do email)
def magic_link_request_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Constrói o link
            link = f"http://{request.get_host()}/accounts/verify/{uid}/{token}/"
            
            # Envia o email (vai aparecer no terminal por causa das tuas settings)
            send_mail(
                'O teu Link Mágico para Portfólio',
                f'Clica aqui para entrar: {link}',
                'noreply@portfolio.com',
                [email],
            )
            return render(request, 'accounts/magic_sent.html')
        except User.DoesNotExist:
            return render(request, 'accounts/magic_request.html', {'error': 'Email não encontrado.'})
    return render(request, 'accounts/magic_request.html')

# View para verificar se o link no email está correto
def magic_link_verify_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        login(request, user)
        return redirect('projetos')
    return render(request, 'accounts/magic_error.html')