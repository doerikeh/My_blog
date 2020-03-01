from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, BlogCategory, BlogSeries
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

def single_slug(request, single_slug):
    categories = [c.category_slug for c in BlogCategory.objects.all()]
    if single_slug in categories:
        matching_series = BlogSeries.objects.filter(blog_category__category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Blog.objects.filter(blog_series__blog_series=m.blog_series).earliest("published")
            series_urls[m] = part_one.blog_slug

        return render(request=request,
                      template_name='categorys.html',
                      context={"blog_series": matching_series, "part_ones": series_urls})

    blog = [t.blog_slug for t in Blog.objects.all()]
    if single_slug in blog:
        this_blog = Blog.objects.get(blog_slug=single_slug)
        blog_from_series = Blog.objects.filter(blog_series__blog_series=this_blog.blog_series).order_by('published')
        this_blog_idx = list(blog_from_series).index(this_blog)

        return render(request=request,
                      template_name='blog.html',
                      context={"blog":this_blog,
                               "sidebar": blog_from_series,
                               "this_blog": this_blog_idx})

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")

def homepage(request):
    blog_catagories = BlogCategory.objects.all()    
    context = {
        'categories': blog_catagories,
    }

    return render(request, "category.html", context)


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"akun baru: {username}")
            login(request, user)
            messages.info(request, f"akun baru: {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = NewUserForm
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, 'Kamu sudah logout')
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Berhasil: {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Username Atau Password Tidak Ada")

    form = AuthenticationForm()
    context = {
        "form": form
    }

    return render(request, "login.html", context)