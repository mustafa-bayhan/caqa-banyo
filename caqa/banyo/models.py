from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import datetime

# Create your models here.

class Ölçüler(models.Model):
    ölçü=models.CharField(null= True,blank=False, max_length=200)
    giriş = models.CharField(max_length=200, default="", null= True, blank=False)
    yükseklik = models.CharField(max_length=200, default="", null= True, blank=False)
    def __str__(self):
        return self.ölçü + ' / ' + self.giriş + ' / ' + self.yükseklik
    
    
class Ürün_model(models.Model):
    isim = models.CharField(null= True,blank=False, max_length=200)
    model_ölçüleri = models.ManyToManyField(Ölçüler, default="", blank=False)

    def __str__(self):
        return self.isim

class Alt_kategoriler(models.Model):
    
    isim = models.CharField(null= True,blank=False, max_length=200)
    def __str__(self):
        return self.isim
     

class Kategoriler(models.Model):
    isim = models.CharField(null= True,blank=False, max_length=200)
    
    def __str__(self):
        return self.isim
    

class Renkler(models.Model):
    renk_ismi =models.CharField(null= True,blank=False, max_length=200)
    renk_resmi = models.ImageField(null=True, upload_to='image/')

    def __str__(self):
        return self.renk_ismi   

class Montaj_tipi(models.Model):
    isim = models.CharField(null= True,blank=False, max_length=200)

    def __str__(self):
        return self.isim  
    
class Ürün (models.Model):
    isim =models.CharField(null= True,blank=False, max_length=200)
    ürün_resmi = models.ImageField(null=True, upload_to='image/')
    kategori= models.ForeignKey(Kategoriler, on_delete= models.CASCADE, related_name='category',null= True, blank=False)
    alt_kategori= models.ForeignKey(Alt_kategoriler, on_delete= models.CASCADE, related_name='Alt_kategori',null= True, blank=False)
    ürün_modelleri= models.ManyToManyField(Ürün_model, default="", blank=False, related_name='type')
    özellikler = RichTextField(null= True)
    montaj_sekli = models.ForeignKey(Montaj_tipi, on_delete= models.CASCADE, related_name='montaj',null= True, blank=False)
    acilis_sekli = models.ImageField(null=True, upload_to='image/')
    renk= models.ManyToManyField(Renkler, default="", blank=False, related_name='color')
    slug = models.SlugField(editable=False, unique=True, null= True, blank=False)
    görüntüleme = models.IntegerField(default = 0)
    def __str__(self):
        return self.isim
    
    
  
    def get_unique_slug(self):
        if not self.pk:
            slug = slugify(self.isim.replace('ı', 'i'))
            unique_slug = slug
        
            counter = 1
            while Ürün.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(slug, counter)
                counter += 1
        else:
            unique_slug=self.slug
        return unique_slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Ürün, self).save(*args, **kwargs)
    
    
class Referanslar(models.Model):
    
    resim = models.ImageField(null=True, upload_to='image/references')
    proje_adi=models.CharField(null= True,blank=False, max_length=200)
    firma=models.CharField(null= True,blank=False, max_length=200)
    adres=models.CharField(null= True,blank=False, max_length=200)
    def __str__(self):
        return self.proje_adi 
    
    
    
class Hakkimizda(models.Model):
    
    
    aciklama = RichTextField(null= True)
    resim = models.ImageField(null=True, upload_to='image/')
    def __str__(self):
        return 'Hakkımızda yazısı'
    
    
class Katalog(models.Model):
    
    katalog_resim = models.ImageField(null=True, upload_to='image/')
    katalog_dosyasi = models.FileField(upload_to ='files/')
    def __str__(self):
        return 'Katalog'
    
    
class Mesajlar(models.Model):
    
    musteri_ismi = models.CharField(max_length=100, verbose_name='Ad Soyad',null= True, blank=False)
    mesaj = models.TextField(max_length=500, verbose_name='Yorum',null= True, blank=False)
    mail= models.EmailField(max_length=100, null= True, blank=False)
    telefon = models.CharField(max_length=12, verbose_name='telefon',null= True, blank=False)
    

    def __str__(self):
        return self.musteri_ismi
   
