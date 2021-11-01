from django import forms
from .models import Post, File, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'text',]

        CATEGORY = (
            (1, '윈도우 센서'),
            (2, '연동 오류'),
            (3, '주소 설정'),
            (4, '회원 정보'),
            (5, '기타 문의'),
            (6, '사용 후기'),
        )

        widgets = {
            'category': forms.Select(choices=CATEGORY, attrs={'class': 'form-control2'}),
            'title': forms.TextInput(attrs={'class': 'form-control2', 'placeholder': '제목을 입력하세요.'}),
            'text': forms.Textarea(attrs={'class': 'form-control2', 'placeholder': '내용을 입력하세요.'}),
        }

        labels = {
            'category': '카테고리',
            'title': '제목',
            # 'image': '첨부파일',
            'text': '내용',
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['path', ]

        labels = {
            'path': '첨부파일',
        }

ImageFormSet = forms.inlineformset_factory(Post, File, form=FileForm, extra=3)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]

        labels = {
            'text': '내용',
        }

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control2', 'placeholder': '내용을 입력하세요.'}),
        }