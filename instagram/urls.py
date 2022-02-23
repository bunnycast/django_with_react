from django.urls import path, re_path, register_converter

from instagram import views


# 정규표현식 커스텀 컨버터 구성 (20으로 시작하는 4자리 숫자)
class YearConverter:
    regex = r"20\d{2}"

    # url에서 추출한 문자열을 뷰에 넘겨주기 전에 변환
    def to_python(self, value):
        return int(value)

    # url reverse시에 호출
    def to_url(self, value):
        return str(value)


register_converter(YearConverter, 'year')

app_name = 'instagram'      # URL Reverse에서 namespace 역할을 하게 됨

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),

    path('archives/<year:year>', views.archive_year),
    # path('archives/2022/', views.archive_year),
    # path('archives/<int:year>/', views.archive_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archive_year),
]