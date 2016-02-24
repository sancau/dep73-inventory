# coding: utf-8
from django.db import models
from datetime import date, timedelta

# Create your models here.

class TestSystem(models.Model):

	PURPOSE_CHOICES = (
			('К', 'Климатические испытания'),
			('М', 'Механические испытания'),
			('В', 'Вакуумные испытания'),
                        ('П', 'Испытания на воздействие пыли'),
		)

	name = models.TextField(verbose_name='Наименование', max_length=200)
	purpose = models.CharField(
		verbose_name='Назначение',
		max_length=1, choices=PURPOSE_CHOICES, 
		null=True
		)
	last_test_date = models.DateField(verbose_name='Дата поверки',null=True)
	next_test_date = models.DateField(verbose_name='Срок поверки',null=True)
	manufacturer = models.CharField(
		verbose_name='Производитель',
		max_length=200
		)
	year_of_production = models.IntegerField(
		verbose_name='Год выпуска',
        null=True
		)
	specification = models.TextField(
		verbose_name='Технические характеристики',
   		max_length=1000
		)
	code = models.CharField(verbose_name='Код', max_length = 50)
	inventory_number = models.CharField(
		verbose_name='Номенклатурный или инвентарный номер',
		max_length = 50
		)
	unit = models.CharField(verbose_name='Единица измерения', max_length = 50)
	price = models.CharField(verbose_name='Цена, руб.', max_length = 50)
	quantity = models.CharField(
		verbose_name='Фактическое наличие (количество)',
		max_length = 50
		)
	total_price = models.CharField(
		verbose_name='Фактическая стоимость (сумма, руб.)',
		max_length = 50
		)
	actual_placement = models.CharField(
		verbose_name='Фактическое расположение',
		max_length = 50
		)

	def test_status(self):
		if self.next_test_date < date.today():
			return 'RED'
		elif self.next_test_date < date.today() + timedelta(days=30):
			return 'YELLOW'
		else:
			return 'GREEN'

	class Meta:
		verbose_name = 'Испытательная система'
		verbose_name_plural = 'Испытательные системы'
		db_table = 'test_systems'

	def __str__(self):
		return self.name

class Tool(models.Model):
	name = models.TextField(verbose_name='Наименование', max_length = 200)
	last_test_date = models.DateField(verbose_name='Дата поверки',null=True)
	next_test_date = models.DateField(verbose_name='Срок поверки',null=True)
	manufacturer = models.CharField(
		verbose_name='Производитель',
		max_length=200,
		)
	year_of_production = models.IntegerField(
		verbose_name='Год выпуска',
        null=True
		)
	specification = models.TextField(
		verbose_name='Технические характеристики',
   		max_length=1000
		)
	code = models.CharField(verbose_name='Код', max_length = 50)
	inventory_number = models.CharField(
		verbose_name='Номенклатурный или инвентарный номер',
		max_length = 50
		)
	unit = models.CharField(verbose_name='Единица измерения', max_length = 50)
	price = models.CharField(verbose_name='Цена, руб.', max_length = 50)
	quantity = models.CharField(
		verbose_name='Фактическое наличие (количество)',
		max_length = 50
		)
	total_price = models.CharField(
		verbose_name='Фактическая стоимость (сумма, руб.)',
		max_length = 50
		)
	actual_placement = models.CharField(
		verbose_name='Фактическое расположение',
		max_length = 50
		)

	def test_status(self):
		if self.next_test_date < date.today():
			return 'RED'
		elif self.next_test_date < date.today() + timedelta(days=30):
			return 'YELLOW'
		else:
			return 'GREEN'
			
	class Meta:
		verbose_name = 'Средство измерений'
		verbose_name_plural = 'Приборы и средства измерений'
		db_table = 'tools'

	def __str__(self):
		return self.name

class MiscItem(models.Model):
	name = models.TextField(verbose_name='Наименование', max_length = 200)
	code = models.CharField(verbose_name='Код', max_length = 50)
	inventory_number = models.CharField(
		verbose_name='Номенклатурный или инвентарный номер',
		max_length = 50
		)
	unit = models.CharField(verbose_name='Единица измерения', max_length = 50)
	price = models.CharField(verbose_name='Цена, руб.', max_length = 50)
	quantity = models.CharField(
		verbose_name='Фактическое наличие (количество)',
		max_length = 50
		)
	total_price = models.CharField(
		verbose_name='Фактическая стоимость (сумма, руб.)',
		max_length = 50
		)
	actual_placement = models.CharField(
		verbose_name='Фактическое расположение',
		max_length = 200
		)

	class Meta:
		verbose_name = 'Инвентарная позиция'
		verbose_name_plural = 'Прочие позиции'
		db_table = 'misc_items'

	def __str__(self):
		return self.name
