import re

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'photo', 'tag_set', 'is_public']
        # exclude = []

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message = re.sub(r'[a-zA-Z]+', '', message)
        return message

    # validators는 가급적 모델에 정의, modelform을 통해 모델의 validators 정보도 같이 가져와야 함

    """
    clean이 필요한 경우
    특정 form에서 1회성 유효성 검사 루틴이 필요할 때
    다수 필드값에 걸쳐 유효성 검사가 필요할 때
    필드 값을 변경해야 할 필요가 있을 때(validator는 값을 체크만 하고, 변경은 안됨   
    """
