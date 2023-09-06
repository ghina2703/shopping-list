from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()

# models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
# Product adalah nama model yang kamu definisikan.
# nama, tanggal_tambah, harga, dan deskripsi adalah atribut atau field pada model. 
# Setiap field memiliki tipe data yang sesuai seperti CharField, DateField, IntegerField, dan TextField.