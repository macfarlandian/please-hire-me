from django.contrib import admin
from portfolio import models
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

# new inline admin subclass, for providing links
# http://www.juripakaste.fi/blog/django-admin-inline-link.html
class LinkedInline(admin.options.InlineModelAdmin):
    template = "portfolio/linked_inline.html"
    admin_model_path = None

    def __init__(self, *args):
        super(LinkedInline, self).__init__(*args)
        if self.admin_model_path is None:
            self.admin_model_path = self.model.__name__.lower()
    
# project details
class ProjectDetailAdmin(PolymorphicChildModelAdmin):
    """ base admin class for detail types """
    base_model = models.ProjectDetail

class ProjectDetailsAdmin(PolymorphicParentModelAdmin):
    """ parent admin for detail types """
    base_model = models.ProjectDetail
    child_models = (
        (models.ImageUpload, ProjectDetailAdmin), 
        (models.VideoEmbed, ProjectDetailAdmin),
        (models.Bullet, ProjectDetailAdmin),
    )
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
        
    
class DetailInline(LinkedInline):
    model = models.ProjectDetail
    fk_name = 'parent'
    extra = 0
    exclude = ['name', 'order', 'desc'] # 'file', 'video'
    # fields = ['order', 'name', 'link']
    # readonly_fields = ['name', 'link']
    # ordering = ['order']
        
    # for adding a new one
    # addurl = reverse('admin:portfolio_projectdetail_add')
    
    # def link(self, obj):
        # url = reverse('admin:portfolio_projectdetail_change', args=(obj.id,))
        # return mark_safe(url)
        # return mark_safe('<a href="{}" target="_blank">(edit)</a>'.format(url))
        
    # link.allow_tags = True
    
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ DetailInline, ]
    prepopulated_fields = {'slug': ('name',)}
    
class ContextAdmin(PolymorphicChildModelAdmin):
    """ base admin class for contexts """
    base_model = models.Context
    prepopulated_fields = {'slug': ('name',)}
    
class ContextsAdmin(PolymorphicParentModelAdmin):
    """ parent admin for contexts """
    base_model = models.Context
    child_models = [
        (models.Job, ContextAdmin),
        (models.Context, ContextAdmin)
    ]
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProjectDetail, ProjectDetailsAdmin)
admin.site.register(models.Context, ContextsAdmin)
admin.site.register(models.Job, ContextAdmin)