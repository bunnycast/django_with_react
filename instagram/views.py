from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from instagram.models import Post


# Create your views here.

# CBV로 손쉽게 구현 (검색 등 세부 기능은 커스텀해야함)
post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


# type hint (python 3.6 이상)
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    pass


def archive_year(request, year):
    return HttpResponse(f"{year}년 archives")