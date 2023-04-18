from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {'posts': list(reversed(posts))}
    return render(request, template, context=context)


def post_detail(request, id):
    template = 'blog/detail.html'
    return render(request, template, context={'post': posts[id]})


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context=context)
