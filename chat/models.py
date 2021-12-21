from datetime import time
from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    allow_users = models.TextField()#1,2,3,4,11,551,61, というような独自のフォーマットを利用する(数字はユーザのID)
    name = models.CharField(max_length=100, blank=False, null=False)#プロジェクト名
    created_at = models.DateTimeField(default=timezone.now)#作成日時(データ追加時に自動で追加されるのでviewsとかで弄る必要はない)
    on_public = models.BooleanField()#プロジェクト一覧ページに公開するかどうか

    def __str__(self):
        return self.name

class Article(models.Model):
    allow_users = models.TextField()#1,2,3,4,11,551,61, というような独自のフォーマットを利用する(数字はユーザのID)
    prj = models.ForeignKey("Project", on_delete=models.CASCADE)#プロジェクトデータへの外部キー
    title = models.CharField(max_length=100)#タイトル
    update_at = models.DateTimeField(default=timezone.now)#更新日時
    content = models.TextField(blank=True, null=True)#内容
