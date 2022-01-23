from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages

from .models import Post
from .forms import CommentForm


class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/posts.html'


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            messages.success(request, 'Thank you, your comment is awaiting approval by Admin')
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, template_name, context)
