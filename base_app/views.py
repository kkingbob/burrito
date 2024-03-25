from django.shortcuts import render

# Create your views here.

posts = [
    {'id':1, 'title':'Installed a bed step'},
    {'id':2, 'title':'Installed a tonneau cover'},
]

def home(request):
    context = {'posts': posts}
    return render(request, 'base_app/home.html', context)

def about(request):
    return render(request, 'base_app/about.html')

def post(request, pk):
    selected_post = None
    for post in posts:
        if post['id'] == int(pk):
            selected_post = post
    context = {'post': selected_post}
    return render(request, 'base_app/post.html', context)