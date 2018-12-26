from django.db import models
from datetime import datetime

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    # untuk membuat judul tiap post = title-nya:
    def __str__(self):
        return self.title
    # untuk membuat nama plural custom utk model kita
    class Meta:
        verbose_name_plural = "Posts"