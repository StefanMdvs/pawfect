from django.shortcuts import render

def blog_posts(request):
    context = {

    }
    return render(request, 'blog/posts.html', context)