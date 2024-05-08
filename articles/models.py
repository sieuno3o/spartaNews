from django.db import models
from django.conf import settings


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    # 작성자 필드 추가
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        db_table = 'comments'


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    url = models.URLField()
    create_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False)
    user_id = models.ForeignKey(
<<<<<<< HEAD
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name = 'articles')

class ArticleLike(models.Model) :
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_likes")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="user_likes")
    
    # like_count =models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name = 'likes',
    #     default=0
    #     )
=======
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles')
>>>>>>> 4a7baa05fcd31f4186c6fe2f32215e9c82f2c460


class ArticleLike(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="article_likes")
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_likes")
    like_count = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes',
        default=0
    )
