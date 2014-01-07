from django.db import models
from embed_video.fields import EmbedVideoField

class ResumeHeader(models.Model):
    """
    Contact and social media information. For a portfolio/site 
    with a single user, this will probably only have one row.
    """
    #attributes
    first_name = models.CharField(max_length=255, 
        help_text="your first name, as it will appear on site and resume")
    last_name = models.CharField(max_length=255, 
        help_text="your last name, as it will appear on site and resume")
    address_street = models.CharField(max_length=255, 
        help_text="your street address, including unit number, as it should appear on your resume", 
        null=True, blank=True)
    address_city = models.CharField(max_length=255, 
        help_text="your city, as it should appear on your resume", 
        null=True, blank=True)
    address_state = models.CharField(max_length=255, 
        help_text="your state, as it should appear on your resume")
    address_zip = models.CharField(max_length=10, 
        help_text="your ZIP code, as it should appear on your resume", 
        null=True, blank=True)
    phone = models.CharField(max_length=255, 
        help_text="your phone number, as it should appear on your resume", 
        null=True, blank=True)
    email = models.CharField(max_length=255, 
        help_text="your email address, as it should appear on your resume", 
        null=True, blank=True)
    website = models.URLField(help_text="your website address, as it should appear on a printed resume", 
        null=True, blank=True)
    linkedin = models.CharField(max_length=30, help_text="your LinkedIn handle", 
        null=True, blank=True)
    twitter = models.CharField(max_length=15, help_text="your Twitter handle", 
        null=True, blank=True)
    other = models.CharField(max_length=255, 
        help_text="any other information you want appear in your resume header", 
        null=True, blank=True)
        
    # admin display name
    def __unicode__(self):
        return "resume header: {} {} ({})".format(self.first_name, 
            self.last_name, self.pk)

class ResumeSection(models.Model):
    """
    A section can be standalone text (e.g., an 'Objective', a list of 'Skills'
    or 'Publications', etc.) or they can be a container for a "collection" of 
    Roles (e.g., an 'Education' section would include schools, 'Experience' 
    would have jobs, etc.).
    """

    name = models.CharField(max_length=255, 
        help_text="title of the section, as it should appear on site and resume")
    header = models.ForeignKey('ResumeHeader', 
        help_text = "the Resume Header this Section should appear under")
    order = models.IntegerField(help_text="integer indicating order within resume")
    roles = models.ManyToManyField('Role',
        help_text="Roles to be collected in this Section, if any",
        null=True, blank=True)
    summary = models.TextField(help_text="additional text or html content to be displayed in this section",
        null=True,blank=True)
    
    # admin display name
    def __unicode__(self):
        return self.name

class Role(models.Model):
    """
    Roles are jobs, degree programs, volunteer positions and other occupations 
    that make up your career history. They serve a dual function. 

    1. Roles can be linked to zero or more Projects. This link is 
       bi-directional: the Projects serve as examples of your work in that Role,
       and the Role provides additional context for that Project.
    2. Roles can be displayed in your resume by collecting them into one or 
       more of the Sections that make up your resume.
    """
    # attributes
    name = models.CharField(max_length=255, 
        help_text="job title, degree program, or other position name")
    slug = models.SlugField(help_text="url-friendly name for this Role")
    order = models.IntegerField(default=0, 
        help_text="integer indicating order within Section")
    org = models.CharField(max_length=255, null=True, blank=True,
        help_text="institution where position was held or degree was obtained")
    startdate = models.DateField(null=True, blank=True,
        help_text="approximate start date of role (YYYY-MM-DD)")
    enddate = models.DateField(blank=True, null=True,
        help_text="approximate end date of role (YYYY-MM-DD)")
    location = models.CharField(max_length=255, null=True, blank=True,
        help_text='location of role (e.g., "San Francisco, CA")')
    summary = models.TextField(null=True,blank=True,
        help_text="short summary of role (for display in a list)")
    long_desc = models.TextField(null=True,blank=True, 
        help_text="long text/html description of this role, for resume display")
    
    # admin display name
    def __unicode__(self):
        return self.name

class Project(models.Model):
    """
    Projects are items in your portfolio. They must exist within a Role, and 
    can include zero or more Details, which are text bullets or multimedia items.
    """
    # attributes
    name = models.CharField(max_length=255)
    role = models.ForeignKey('Role', 
        help_text="Role this Project is related to")
    slug = models.SlugField(help_text="url-friendly name for this Project")
    order = models.IntegerField(default=0,
        help_text="integer indicating display order on your site")
    completion_date = models.DateField(null=True, blank=True,
        help_text="approximate completion date of project (YYYY-MM-DD)")
    summary = models.TextField(null=True,blank=True,
        help_text="short summary of Project (for display in a list)")
    index_image = models.ImageField(upload_to='images/', null=True, blank=True, 
        help_text="upload an image file for display in project list")
    intro = models.TextField(null=True,blank=True, 
        help_text="longer text/html introductory description of this Project")
        
    # "details" : reverse foreign keys
    
    # configuration options
    class Meta:
        ordering = ['order']

    # admin display name
    def __unicode__(self):
        return self.name
    
class Detail(models.Model):
    """
    Details are text bullets or multimedia items (photo/video) that can be 
    attached to a Project to provide a fuller description of the Project.
    """
    name = models.CharField(max_length=255,
        help_text="title of detail (can be alt text for an image)")
    project = models.ForeignKey(Project, related_name="details",
        help_text="Project that will include this Detail")
    order = models.IntegerField(default=0,
        help_text="integer indicating order within Project")
    desc = models.TextField(null=True,blank=True,
        help_text="text description or caption")
    img = models.ImageField(upload_to='images/', null=True, blank=True, 
        help_text="upload an image file to create a visual bullet or slideshow slide")
    video = EmbedVideoField(null=True, blank=True,
        help_text="paste a YouTube, Vimeo or SoundCloud URL to embed it on your project page")
    
    # configuration options
    class Meta:
        ordering = ['order']

    # admin display name
    def __unicode__(self):
        return self.name
