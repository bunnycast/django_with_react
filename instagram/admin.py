from django.contrib import admin
from instagram.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    # # model에서 함수 쓰는 것과 똑같은 효과
    # def message_length(self, post):
    #     return f"{len(post.message)} 글자"
    #
    # message_length.short_description = "메시지 글자 수"
