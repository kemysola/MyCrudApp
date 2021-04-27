

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from .models import Article
from .forms import CommentForm 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from django.urls import reverse 


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/articles.html',{'articles':articles})


@login_required(login_url ='/accounts/login/')
def article_details(request,slug,):
    template_name ='articles/article_detail.html'
    post = get_object_or_404(Article, slug=slug)
    comments =post.comments.filter(active=True)
    new_comment = None
    if request.method =='POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()
        
    return render(request,template_name,{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})
    

#add a decorator.import decorator to redirect to login





@login_required(login_url ='/accounts/login/')
def article_create(request):
    if request.method =='POST':
        form = forms.CreateArticle(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            #save to db
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
        
    form =forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})

