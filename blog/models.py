from django.db import models
from django.utils import timezone

# Create your models here.

#models.Model means that Post is a Django Model, so Django knows it should be saved in database
class Post(models.Model):

	#link to another model
	author = models.ForeignKey('auth.User')
	#define limit for number of characters
	title = models.CharField(max_length=200)
	#for long text without limits, suitable for blog post
	text = models.TextField()
	#date and time
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
	
