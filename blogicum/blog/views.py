from django.shortcuts import render, get_list_or_404, get_object_or_404
from blog.models import Post, Category
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.select_related(
            'category'
        ).published().filter(pub_date__date__lte=datetime.now())[:5]
    context = {'post_list': posts}
    return render(request, template, context=context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'category'
        ).published().filter(id=id, pub_date__date__lte=datetime.now())
    )
    return render(request, template, context={'post': post})


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(slug=category_slug,
                                is_published=True)
    )
    post_list = get_list_or_404(
        category.posts.published().filter(
            pub_date__date__lte=datetime.now()
        )
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context=context)
