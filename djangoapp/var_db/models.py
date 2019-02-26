from django.db import models
from django.utils import timezone

class Chromosome(models.Model):
	
	name = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return(self.name)

class Variant(models.Model):
	
	position = models.IntegerField(null=False)
	change = models.CharField(max_length=200)
	pathogenic = models.NullBooleanField(null=True)
	submitter = models.CharField(max_length=200, default='unknown')
	chromosome = models.ForeignKey(Chromosome, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return "{} {}".format(self.position, self.change)

	def get_hgvs(self):
		hgvs = str(self.position) + ':' + self.change
		return hgvs



