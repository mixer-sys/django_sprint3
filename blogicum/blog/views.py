from django.shortcuts import render, get_list_or_404, get_object_or_404
from blog.models import Post, Category
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.select_related(
            'category'
        ).filter(is_published=True, pub_date__date__lte=datetime.now(),
                 category__is_published=True).order_by('-pub_date')[:5]

    context = {'post_list': list(reversed(posts))}
    return render(request, template, context=context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'category'
        ).filter(id=id, pub_date__date__lte=datetime.now(),
                 is_published=True, category__is_published=True)
    )
    return render(request, template, context={'post': post})


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(slug=category_slug,
                                is_published=True)
    )
    post_list = get_list_or_404(
        Post.objects.select_related(
            'category'
        ).filter(
            category__slug=category_slug,
            is_published=True,
            pub_date__date__lte=datetime.now(),
            category__is_published=True
        )
    )

    context = {'category': category, 'post_list': post_list}
    return render(request, template, context=context)
