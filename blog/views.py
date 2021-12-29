from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from .models import Post, Contact
from .forms import PostForm, ContactForm
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post_to_remove = Post.objects.get(pk=pk)
    post_to_remove.delete()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return redirect('post_list')

def about(request):
    about_name = "О блоге"
    about_disc = "Описание блога в процессе..."
    return render(request, 'blog/about_template.html', {'about_name': about_name, 'about_disc': about_disc })

class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm


def success(request):
   return render(request, 'blog/success.html', {})