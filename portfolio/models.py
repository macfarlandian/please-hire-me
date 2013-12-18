from django.db import models
from embed_video.fields import EmbedVideoField
from polymorphic import PolymorphicModel

"""
CONTEXT DETAIL
- bullet text
"""

class Project(models.Model):
    """
    Project
    - name
    - slug
    - summary
    - date
    - PROJECT DETAIL(S) in order
    - assoc. CONTEXT
    """
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    slug = models.SlugField()
    date = models.DateField()
    summary = models.TextField()
    context = models.ForeignKey('Context', related_name = 'projects')

    def __unicode__(self):
        return self.name
              
    class Meta:
        ordering = ['order']
    
# base for all detail classes 
class Detail(PolymorphicModel):
    
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    desc = models.TextField(null=True,blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order']
        # abstract = True
        verbose_name = 'detail'    

# project detail models
class ProjectDetail(Detail):
    """ 
    *Project Detail Kinds*
    ImageUpload
    YouTubeEmbed
    Bullet
    """
    parent = models.ForeignKey(Project, related_name="details")
    
    class Meta:
        verbose_name = "detail"
    
        
class ImageUpload(ProjectDetail):
    file = models.FileField(upload_to='images/')
    class Meta:
        verbose_name = 'image'

class VideoEmbed(ProjectDetail):
    video = EmbedVideoField()
    class Meta:
        verbose_name = 'video embed'
    
class Bullet(ProjectDetail):
    # don't need any additional fields for this right now
    class Meta:
        verbose_name = 'bullet'    
    
# for jobs and shit
class Context(PolymorphicModel):
    """
    Contexts
    - kind (job, education, personal, etc)
    - org
    - job title
    - slug
    - startdate
    - enddate
    - CONTEXT DETAIL(S) in order
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name
        
class Job(Context):
    org = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "job"
        ordering = ['-startdate']
    
class JobDetail(Detail):
    parent = models.ForeignKey(Job, related_name="details")
    
class School(Context):
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = "school"
    
class SchoolDetail(Detail):
    parent = models.ForeignKey(School, related_name="details")

# more resume fields
class SkillArea(Detail):
    class Meta:
        verbose_name = "skill area"

class Skill(Detail):
    parent = models.ForeignKey(SkillArea, related_name="skills")
    
class Award(Detail):
    org = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    
    