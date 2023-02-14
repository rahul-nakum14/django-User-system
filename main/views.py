from django.shortcuts import render, redirect
from .forms import UserRegisterForm , post_form
from . models import post_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/login')
def home(request):
    if request.user.is_authenticated:
        private_posts = post_model.objects.filter(author=request.user, is_private=True)
        public_posts = post_model.objects.filter(is_private=False)
        posts = private_posts | public_posts
    else:
        posts = post_model.objects.filter(is_private=False)

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = post_model.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    
    return render(request, 'main/home.html', {'posts': posts})

def delete_post(request):
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = post_model.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    
    return render(request, 'main/home.html')
   
def update_post(request, post_id):
    post = post_model.objects.get(id=post_id)
    if request.method == "POST":
        form = post_form(request.POST, instance=post) 
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = post_form(instance=post)
    return render(request, 'main/update_post.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('sign_up')
            else:
                form.save()
                messages.success(request, 'Account Is Created')
                return redirect('sign_up')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})


@login_required(login_url='/login')
def create_post(request):
  if request.method == "POST":
    form = post_form(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("/home")
  else:
        form = post_form()
  return render(request,"main/post.html",{'form':form})





# def login_data(request):
#     form = UserRegisterForm(request.POST)
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username,password=password)

#         if user is not None:
#                login(request,user)
#                return redirect('home')
#         else:
#                 messages.error(request, 'Invalid login credentials')
#                 return redirect('login')
        
#     return render(request, 'registration/login.html', {'form': form})
# def login_data(request):
#     form = signupform(request.POST)
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password1']

#         user = authenticate(username=username,password=password)

#         if user is not None:
#                login(request,user)
#                return redirect('index')
#         else:
#                 messages.error(request, 'Invalid login credentials')
#                 return redirect('login')
        
#     return render(request, 'main/login.html', {'form': form})



# @login_required(login_url='/login')
# def home(request):
#   posts = post_model.objects.all()
#   if request.method == "POST":
#      post_id = request.POST.get("post-id")
#      post = post_model.objects.filter(id=post_id).first()
#      if post and post.author == request.user:
#         post.delete()
#   return render(request, 'main/home.html',{'posts':posts})




# @login_required(login_url='/login')
# def home(request):
#     if request.method == "POST":
#       form = post_form(request.POST)
#       if form.is_valid():
#           private = form.cleaned_data.get('is_private')
#           if not private:
#               posts = post_model.objects.all()
#           else:
#               posts = post_model.objects.filter(author=request.user)
#       else:
#         form = post_form()
#     return render(request, 'main/home.html', {'posts': posts, 'form': form})






# @login_required(login_url='/login')
# def home(request):
#     form = post_form(request.POST or None)
#     posts = []
#     if form.is_valid():
      
#       if request.user.is_authenticated:
#           posts = post_model.objects.exclude(is_private=True)
#       else:
#           posts = post_model.objects.exclude(is_private=False)

#     else:
#         form = post_form()

#     return render(request, 'main/home.html', {'posts': posts, 'form': form})



# @login_required(login_url='/login')
# def home(request):
#     form = post_form(request.POST or None)
#     posts = post_model.objects.all()
#     if form.is_valid():
#         posts = post_model.objects.all().values('is_private')

#         for post in posts:
#           if post['is_private']:
#               posts = posts.exclude(is_private=False)
#           else:
#               posts = posts.exclude(is_private=True)
#     else:
#         form = post_form()
#     return render(request, 'main/home.html', {'posts': posts, 'form': form})