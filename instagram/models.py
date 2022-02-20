from django.db import models


# Create your models here.

class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')  # upload_to = media_root 하위에 저장 경로 추가
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    def message_length(self):
        return f"{len(self.message)} 글자"

    message_length.short_description = "메시지 글자 수"
