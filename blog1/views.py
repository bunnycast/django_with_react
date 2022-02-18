from django.shortcuts import render
from blog1.models import Post


# Create your views here.

def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog1/post_list.html', {
        'post_list': qs,
    })
