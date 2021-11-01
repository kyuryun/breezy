from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import *
from django.http import Http404
from .forms import PostForm, ImageFormSet, CommentForm
from django.db import transaction
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/index.html'

class AboutView(TemplateView):
    template_name = 'home/about.html'

class ServiceView(TemplateView):
    template_name = 'home/service.html'

class ReviewList(ListView):
    queryset = Post.objects.filter(category=6).order_by('-published_date', '-postCode')
    template_name = 'home/review_list.html'
    paginate_by = 4

def review_detail(request, pk):
    try:
        object = Post.objects.get(pk=pk)
        image = object.post_file.all()
        comment = object.post_id.all()
    except Post.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'home/review_detail.html', {'object' : object, 'image' : image, 'comments':comment})


def post_new(request):
    form = PostForm(request.POST)
    image_formset = ImageFormSet(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid() and image_formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            with transaction.atomic():
                post.save()
                image_formset.instance = post
                image_formset.save()
                return redirect('/review/')
    else:
        form = PostForm()
        image_formset = ImageFormSet()
    return render(request, 'home/upload.html', {'form': form, 'image_formset':image_formset})

# 게시글 삭제
def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/review/')
    return render(request, 'home/delete.html', {'Post':post})

# 게시글 수정
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=post)
        if form.is_valid() and image_formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            with transaction.atomic():
                post.save()
                image_formset.instance = post
                image_formset.save()
                return redirect('/review/')
    else: # "GET" 메서드일 때
        form = PostForm(instance=post) # 이전에 있던 데이터를 넣어서 보여줌
        image_formset = ImageFormSet(instance=post)
    return render(request, 'home/edit.html', {'form':form, 'image_formset':image_formset})


# 문의 게시판 목록보기
class PostList(ListView):
    queryset = Post.objects.exclude(category=6).order_by('-published_date', '-postCode')
    template_name = 'home/post_list.html'
    paginate_by = 10


def post_new2(request):
    form = PostForm(request.POST)
    image_formset = ImageFormSet(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid() and image_formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            with transaction.atomic():
                post.save()
                image_formset.instance = post
                image_formset.save()
                return redirect('/post/')
    else:
        form = PostForm()
        image_formset = ImageFormSet()
    return render(request, 'home/upload.html', {'form': form, 'image_formset':image_formset})


def post_detail(request, pk):
    try:
        object = Post.objects.get(pk=pk)
        image = object.post_file.all()
        comment = object.post_id.all()
    except Post.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'home/post_detail.html', {'object' : object, 'image' : image, 'comments':comment})


# 게시글 삭제
def remove_post2(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/post/')
    return render(request, 'home/delete_post.html', {'Post':post})

# 게시글 수정
def edit_post2(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=post)
        if form.is_valid() and image_formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            with transaction.atomic():
                post.save()
                image_formset.instance = post
                image_formset.save()
                return redirect('/post/')
    else: # "GET" 메서드일 때
        form = PostForm(instance=post) # 이전에 있던 데이터를 넣어서 보여줌
        image_formset = ImageFormSet(instance=post)
    return render(request, 'home/edit.html', {'form':form, 'image_formset':image_formset})


# def comment_write(request, post_pk):
#     if request.method == 'POST':
#         post = get_object_or_404(Post, pk=post_pk)
#         content = request.POST.get('content')
#         author = request.user
#         published_date = timezone.now()
#
#         Comment.objects.create(author=author, postCode=post, text=content, published_date=published_date).save()
#         return redirect('/review/')

@login_required
def comment_new(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()

            post = get_object_or_404(Post, pk=pk)
            comment.postCode = post
            comment.save()
            return redirect('home:review_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'home/comment.html', {'form': form})

@login_required
def comment_new2(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()

            post = get_object_or_404(Post, pk=pk)
            comment.postCode = post
            comment.save()
            return redirect('home:post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'home/comment.html', {'form': form})

# FAQ 화면
class FAQView(TemplateView):
    template_name = 'home/post_faq.html'