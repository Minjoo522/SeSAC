from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=False)
    # DB에는 경로에 대한 url이 들어가고, 사진은 photos/ 폴더를 만들어서 업로드
    image = models.ImageField(upload_to='photos/', null=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, {self.image}'