from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

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
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#   # step 1. 단순 orm 쿼리, Post.DoesNotExist 예외처리 불가
#     post = Post.objects.get(pk=pk)
#
#     # Step 2. try catch
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#
#     # step 3. get_object_or_404 메소드로 한줄에 처리
#     post = get_object_or_404(Post, pk=pk)
#
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })

# step 4. CBV generic > DetailView로 FBV를 한줄로 작성
post_detail = DetailView.as_view(model=Post)


def archive_year(request, year):
    return HttpResponse(f"{year}년 archives")