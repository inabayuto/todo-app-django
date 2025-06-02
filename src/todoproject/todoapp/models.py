from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # ユーザー
    title = models.CharField(max_length=200) # タイトル
    description = models.TextField() # 説明
    completed = models.BooleanField(default=False) # 完了フラグ
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時
    updated_at = models.DateTimeField(auto_now=True) # 更新日時

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']