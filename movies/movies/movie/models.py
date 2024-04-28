from django.db import models
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    movie_image = models.ImageField(upload_to='movie/images',null=True)
    movie_name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)
    part = models.IntegerField(default=1)
    director = models.ForeignKey(to='director.Director', on_delete=models.CASCADE)
