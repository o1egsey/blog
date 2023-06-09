from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import PostModel, Profile
from .forms import PostModelForm, PostUpdateForm, CommentForm, ProfileForm
from account.models import UserBase


# @login_required
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in first!')
        return redirect('account:login')
    else:
        posts = PostModel.objects.all()
        context = {
            "posts": posts,
        }
        return render(request, "home.html", context)


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, "Blog Post posted successfully!")
            return redirect("blog:blog-index")
    else:
        form = PostModelForm()
    context = {
        "form": form,
    }

    return render(request, "blog/post.html", context)


@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:blog-post-detail", pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        "post": post,
        "form": form,
    }
    return render(request, "blog/post_edit.html", context)


@login_required
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    comments = post.comments()
    if request.method == "POST":
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            messages.success(request, "Коментар додано успішно!")
            return redirect("blog:blog-post-detail", pk=post.id)
    else:
        c_form = CommentForm()
    context = {"post": post, "c_form": c_form, "comments": comments, 'user': request.user}
    return render(request, "blog/post_detail.html", context)


def view_profile(request):
    return render(request, "blog/profile.html")


@login_required
def profile_edit(request, id):
    user = UserBase.objects.get(id=id)

    if Profile.objects.filter(user_id=id).exists():
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)

    if request.method == "POST":
        if request.user != user:
            return HttpResponse(
                "У вас нет прав на изменение этой информации пользователя."
            )

        profile_form = ProfileForm(request.POST)

        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.firstname = profile_cd["firstname"]
            profile.lastname = profile_cd["lastname"]
            profile.age = profile_cd["age"]
            profile.gender = profile_cd["gender"]
            profile.website = profile_cd["website"]
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("blog:profile_edit", id=id)
        else:
            return HttpResponse("Щось пішло не так. Спробуйте інші дані.")

    elif request.method == "GET":
        profile_form = ProfileForm()
        context = {"profile_form": profile_form, "profile": profile, "user": user}
        return render(request, "blog/profile.html", context)
    else:
        return HttpResponse("Використовуйте тільки GET/POST запити")


def create_test_data(request):
    user = UserBase.objects.create_user(user_name='te1est1__userr1',
                                        password='test1password',
                                        email='test11r@user.com')

    for i in range(1000):
        post = PostModel(title=f'Test Post {i}',
                         content='Test Content',
                         author=user,
                         is_test_data=True)
        post.save()

    return HttpResponse('Test data created successfully')


def clean_test_data(request):
    PostModel.objects.filter(is_test_data=True).delete()

    return HttpResponse('Test data cleaned successfully')
