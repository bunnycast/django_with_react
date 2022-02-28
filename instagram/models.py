from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')  # upload_to = media_root 하위에 저장 경로 추가
    tag_set = models.ManyToManyField('instagram.Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    def message_length(self):
        return f"{len(self.message)} 글자"

    message_length.short_description = "메시지 글자 수"

    # post_detail에 대한 get_absolute_url 함수를 작성하면 url 관리가 수월해진다
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE,
                             limit_choices_to={'is_public': True})  # post_id 필드가 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField('instagram.Post')

    def __str__(self):
        return self.name
