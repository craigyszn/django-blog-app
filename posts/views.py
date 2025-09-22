from django.shortcuts import render


# sample data (instead of using a database model for now)
posts = [
    {"title": "First Post", "content": "Welcome to my blog!"},
    {"title": "Second Post", "content": "Django makes development fun."},
]

def home(request):
    return render(request, "posts/home.html", {"posts": posts})

