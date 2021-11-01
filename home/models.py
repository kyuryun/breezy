from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

# 회원 테이블
class MyUser(AbstractUser):
    username = models.CharField(max_length=20, primary_key=True)
    phone = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.username

    def register(self):
        self.reg_date = timezone.now()
        self.save()

MyUser = get_user_model()


# 문의유형 테이블
class Category(models.Model):
    code = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=10)

    def __str__(self):
        return str(self.category)

    class Meta:
        ordering = ['code']
        verbose_name_plural = 'Categories'


# 게시글 테이블
class Post(models.Model):
    postCode = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='post_user_id')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='post/%Y/%m/%d', default='post/review_img.png', blank=True) # default='post/no_image.png'
    text = models.TextField()
    published_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']
        abstract = False

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# 첨부파일 테이블
class File(models.Model):
    fileCode = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to='post/%Y/%m/%d', default='post/no_image.png')
    postCode = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_file')

    def __str__(self):
        return str(self.fileCode)

    class Meta:
        ordering = ['fileCode']


# 댓글 테이블
class Comment(models.Model):
    commentCode = models.AutoField(primary_key=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_id')
    postCode = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_id')
    text = models.TextField()
    published_date = models.DateField(blank=True, null=True, auto_now_add=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['commentCode']
