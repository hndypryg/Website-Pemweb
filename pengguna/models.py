from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True, null=True)
    telpon = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='pengguna', blank=True, null=True)

    def _str_(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "1. Biodata"
    
from django.db import models

# One to One
class Orang(models.Model):
    name = models.CharField(max_length=100)
    paspor = models.OneToOneField('Paspor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "'s Paspor"

class Paspor(models.Model):
    number = models.CharField(max_length=20)
    expiration_date = models.DateField()

    def __str__(self):
        return self.number

# Penjelasan relasi antar tabel:
# 1. One to One (Orang to Paspor):
#    OneToOne model berisi data yang hanya berlaku untuk satu objek,    
#    Setiap Orang terkait dengan satu Paspor, dan setiap Paspor hanya terkait dengan satu Orang,
#    Dengan menggunakan OneToOneField di model Orang yang mengacu pada model Paspor.
    
# One to Many
class Penulis(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Buku(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Penulis, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# 2. One to Many (Penulis to Buku):
#    OneToMany model berisi data yang berlaku untuk satu objek, tetapi dapat memiliki banyak objek lainnya,
#    Setiap Penulis dapat memiliki banyak Buku, tapi setiap buku hanya dimiliki oleh satu penulis,
#    Dengan menggunakan ForeignKey di model Buku yang mengacu pada model Penulis.

# Many to Many
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField()

    def __str__(self):
        return self.title

# 3. Many to Many (Film to Genre):
#    ManyToMany model berisi data yang berlaku untuk banyak objek, tetapi hanya dapat memiliki banyak objek lainnya,
#    Banyak Film dapat memiliki banyak Genre, dan sebaliknya, banyak Genre dapat diterapkan pada banyak film,
#    Dengan menggunakan ManyToManyField di model Film yang mengacu pada model Genre.