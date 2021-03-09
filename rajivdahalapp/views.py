from django.shortcuts import render
from django.http import HttpResponse
from . models import Message,Post,Blog,Trendingpost,Mainpost
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        message=Message(name=name,email=email,subject=subject,message=message)
        message.save()

    return render(request,'home.html') 

def post(request):
    


    trendingpost=Trendingpost.objects.all()
    paginator1=Paginator(trendingpost,3)
    page_number1=request.GET.get('page')
    page_obj1=paginator1.get_page(page_number1)
    

    

    mainpost=Mainpost.objects.all()
    paginator2=Paginator(mainpost,2)
    page_number2=request.GET.get('page')
    page_obj2=paginator2.get_page(page_number2)


    context={'post':post,'trendingpost':page_obj1,'mainpost':page_obj2}
   



    return render(request,'post.html',context) 
def blogs(request):
    blog=Blog.objects.all()
    context={'blog':blog}
    print(context)


    return render(request,'blogs.html',context)     

def more(request):
    return render(request,'more.html')     

def viewpost(request,slug_text):
    
    post=Post.objects.filter(slug=slug_text)
    context={'post':post}
    return render(request,'viewpost.html',context)   

def viewblog(request,slug_text):
    blog=Blog.objects.filter(slug=slug_text)
    context={'blog':blog}
    print(context)
    
    return render(request,'viewblog.html',context)    

def trendingpost(request,slug_text):
    
    post=Trendingpost.objects.filter(slug=slug_text)
    context={'post':post}
    return render(request,'trendingpost.html',context)
     
    
