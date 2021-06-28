from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=200, verbose_name='Название услуги')
	price = models.PositiveIntegerField(verbose_name='Цена')

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'

	def __str__(self):
		return self.name


class Makeup_img(models.Model):
	image = models.ImageField(upload_to='makeup/', verbose_name='Фото')

	class Meta:
		verbose_name = 'Фото макияжа'
		verbose_name_plural = 'Фотки макияжа'

	def __str__(self):
		return str(self.image.name)


class Wedding_img(models.Model):
	image = models.ImageField(upload_to='wedding/', verbose_name='Фото')

	class Meta:
		verbose_name = 'Фото свадебного образа'
		verbose_name_plural = 'Фотки свадебных образов'

	def __str__(self):
		return str(self.image.name)


class Hair_img(models.Model):
	image = models.ImageField(upload_to='hair/', verbose_name='Фото')

	class Meta:
		verbose_name = 'Фото прически'
		verbose_name_plural = 'Фотки причесок'

	def __str__(self):
		return str(self.image.name)