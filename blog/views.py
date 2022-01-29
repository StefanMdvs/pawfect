from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CommentForm, PostForm


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
            messages.success(request, 'Thank you, your comment is \
                awaiting approval by Admin')
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'on_blog_page': True
    }

    return render(request, template_name, context)


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin can access this section')
        return redirect(reverse('posts'))

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Failed to add blog post. Check if form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog_post(request, slug):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin can access this section')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated \
                {post.title}!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, f'Failed to update {post.title}. \
                Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_blog_post(request, post_id):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin can access this section')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(Post, pk=post_id)
    blog_post.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('posts'))