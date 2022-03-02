from django.urls import path, re_path, register_converter

from instagram import views
from instagram.converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, "day")

app_name = 'instagram'      # URL Reverse에서 namespace 역할을 하게 됨

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),

    # path('archives/<year:year>', views.archive_year, name='archive year'),
    # path('archives/2022/', views.archive_year),
    # path('archives/<int:year>/', views.archive_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archive_year),

    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<int:year>', views.post_archive_year, name='post_archive_year'),
    # path('archive/<int:year>/<int:month>/', views.post_archive_month, name='post_archive_month'),
    # path('archive/<int:year>/<int:month>/<int:day>/', views.post_archive_day, name='post_archive_day'),
]
