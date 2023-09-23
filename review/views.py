from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def get_map(request):
    MAPS_API_KEY = settings.MAPS_API_KEY
    return render(request, 'main/searchstation.html', {MAPS_API_KEY: MAPS_API_KEY})


def get_searchstation(request):
    return render(request, 'main/searchstation.html')


def get_contact(request):
    return render(request, 'main/contact.html')


def get_review(request):
    return render(request, 'main/review.html')


def get_join(request):
    return render(request, 'main/join.html')


def get_login(request):
    return render(request, 'main/login.html')


@login_required
def get_write_review(request):
    submitted = False
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            messages.success(request, 'Your review has been successfully posted.')
            return redirect('review')
    else:
        form = PostForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/post_review.html', {'form': form})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'main/review.html'
    context_object_name = 'post_list'
    paginate_by = 6


def edit_review(request, slug):
    review = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            messages.success(request, 'Your review has been successfully changed.')
            return redirect('review')

    form = PostForm(instance=review)
    success_url = reverse_lazy('review')
    return render(request, 'main/edit_review.html', {'form': form, 'review': review})


def delete_review(request, slug):
    review = get_object_or_404(Post, slug=slug)
    review.delete()
    messages.success(request, 'Your review has been successfully removed.')
    return redirect('review')
