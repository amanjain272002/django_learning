from django.shortcuts import render, HttpResponse
from blog.models import Post
from home.models import Contact 
from django.contrib import messages
from home.models import postt


# Create your views here.
def home(request): 
    return render(request,'home/home.html')

# def about(request):
#     # message.success(request,"This is about")
#     return render(request,'home/about.html')
#     # return HttpResponse("This is contact")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, 'home/search.html', params)

def about(request):
    if request.method=="POST":
        writepost=request.POST['writepost']
        writecontent = request.POST['writecontent']
        about=postt(writepost=  writepost ,writecontent=writecontent)
        about.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, "home/about.html")

    