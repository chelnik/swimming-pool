from datetime import date
from django.apps import apps
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pool_app.models import PoolPass
from .forms import UserCustomForm


User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        form = UserCustomForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('users:login')
    else:
        form = UserCustomForm()
    return render(
        request, 'users/registration.html', {'form': form}
    )


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pool_app:index')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required
def user_detail(request):
    user = request.user
    pool_pass = user.active_pool_pass
    signed_up_lessons = user.lessons.all()
    age = None

    if user.active_pool_pass:
        user.active_pool_pass.check_activation()

    if user.date_of_birth:
        today = date.today()
        age = (
                today.year - user.date_of_birth.year -
                ((today.month, today.day) < (user.date_of_birth.month,
                                             user.date_of_birth.day))
        )

    if user.date_of_birth:
        today = date.today()
        age = (
            today.year - user.date_of_birth.year -
            ((today.month, today.day) < (user.date_of_birth.month,
                                         user.date_of_birth.day))
        )

    if request.method == 'POST':
        form = UserCustomForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:user_detail')
    else:
        form = UserCustomForm(instance=user)

    context = {
        'form': form,
        'age': age,
        'pool_pass': pool_pass,
        'signed_up_lessons': signed_up_lessons
    }

    if user.is_staff:
        users = User.objects.all()
        context['users'] = users

    return render(request, 'users/user_detail.html', context)
