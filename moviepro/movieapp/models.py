from django.db import models

class Telugu_Movies(models.Model):
    movie_name=models.CharField(max_length=300)
    director_name=models.CharField(max_length=50)
    Hero_name=models.CharField(max_length=50)
    Heroiene_name=models.CharField(max_length=50)
    producer_name=models.CharField(max_length=50)
    released_date=models.DateField(max_length=50)

    def __str__(self):
        return self.director_name

class Hindi_Movies(models.Model):
    movie_name=models.CharField(max_length=300)
    director_name=models.CharField(max_length=50)
    Hero_name=models.CharField(max_length=50)
    Heroiene_name=models.CharField(max_length=50)
    producer_name=models.CharField(max_length=50)
    released_date=models.DateField(max_length=50)

class English_Movies(models.Model):
    movie_name = models.CharField(max_length=300)
    director_name = models.CharField(max_length=50)
    Hero_name = models.CharField(max_length=50)
    Heroiene_name = models.CharField(max_length=50)
    producer_name = models.CharField(max_length=50)
    released_date = models.DateField(max_length=50)




class Book_Movie_Data(models.Model):
    movie_name=models.CharField(max_length=50)
    theater_name=models.CharField(max_length=50)
    show_time=models.CharField(max_length=50)
    select_seats=models.IntegerField()
    select_date=models.DateField(max_length=100)
