from django.db import models

class SubjectType(models.Model):
	name = models.CharField(max_length = 100)

	def __unicode__(self):
		return unicode(self.name)

class Subject(models.Model):
	subject_type = models.ForeignKey(SubjectType)
	name = models.CharField(max_length = 100)

	def __unicode__(self):
		return unicode(self.subject_type) + ": " + unicode(self.name)