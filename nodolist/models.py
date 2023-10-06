from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(_("tag_name"), max_length=50)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    # 時間は5分刻みにできるようにchoicesを作る
    tasks = models.CharField(max_length=40, blank=False, null=False)
    text = models.TextField(blank=True, null=True)
    complete_time = models.IntegerField(blank=False, null=False)
    is_done = models.BooleanField(_("完了フラグ"), default=False)
    tags = models.ManyToManyField(Tag, verbose_name=_("Tagモデルのname"), blank=True)
    created_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tasks


class Image(models.Model):
    img = models.ImageField(upload_to="images/")
