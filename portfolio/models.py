from django.db import models
from embed_video.fields import EmbedVideoField

class Project(models.Model):
    """ entries in the portfolio """
    # attributes
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    order = models.IntegerField(default=0)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    
    # relationships
    context = models.ForeignKey('Context', related_name = 'projects', 
        null=True, blank=True)
    # details: reverse foreign keys
    
    # configuration options
    class Meta:
        ordering = ['order']

    # admin display name
        def __unicode__(self):
            return self.name
    
class Detail(models.Model):
    """ in depth details for Projects """
    # attributes
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    desc = models.TextField(null=True,blank=True)
    img = models.FileField(upload_to='images/', null=True, blank=True)
    video = EmbedVideoField(null=True, blank=True)
    
    # relationships
    project = models.ForeignKey(Project, related_name="details")
    
    # configuration options
    class Meta:
        ordering = ['order']

    # admin display name
    def __unicode__(self):
        return self.name
    
class Context(models.Model):
    """ related to projects, included in resume """
    # attributes
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    org = models.CharField(max_length=255, null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(null=True,blank=True)
    
    # relationships
    # projects: reverse foreign keys
    
    # configuration options
    class Meta:
        pass
    
    # admin display name
    def __unicode__(self):
        return self.name
        
class Resume(models.Model):
    """ it's a resume """
    # attributes
    name = models.CharField(max_length=255)
    # name
    fname = models.CharField(max_length=255, verbose_name='first name')
    lname = models.CharField(max_length=255, verbose_name='last name')
    # address
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True, 
        verbose_name='ZIP')
    
    # contact info
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=30, null=True, blank=True)
    twitter = models.CharField(max_length=15, null=True, blank=True)
    etc = models.CharField(max_length=255, null=True, blank=True)
    
    # relationships
    blocks = models.ManyToManyField('Block')
    
    # configuration options
    class Meta:
        pass
    
    # admin display name
    def __unicode__(self):
        return "resume: {}".format(self.name)
        
class Block(models.Model):
    """ sections of a resume """
    # attributes
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True,blank=True)
    
    # relationships
    collection = models.ManyToManyField('Context')
    sub = models.ManyToManyField('self')
    
    # configuration options
    class Meta:
        pass
    
    # admin display name
    def __unicode__(self):
        return "block: {}".format(self.name)