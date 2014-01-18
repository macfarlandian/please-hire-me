from django.contrib import admin
from . import models

# DRY: set some common options first and inherit
class RichTextAdmin(admin.ModelAdmin):
    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js']
            
class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
class ReorderAdmin(admin.ModelAdmin):
    list_editable = ['order']
    list_display_links = ['name'] # so you can put order first

def _summary(obj):
    """access summary field as callable to allow HTML display"""
    return obj.summary
_summary.allow_tags = True

class HeaderAdmin(RichTextAdmin):
    exclude = ['img_width', 'img_height']

class SectionAdmin(RichTextAdmin, ReorderAdmin):
    filter_horizontal = ['roles']
    list_display = ['order', 'name', _summary, 'header']
    
class RoleAdmin(SlugAdmin, RichTextAdmin, ReorderAdmin):
    def getSection(self, role):
        """retrieve name of related section"""
        rel = role.section.all()
        if len(rel):
            return rel[0]
        else:
            return None
    getSection.short_description = 'Section'
    getSection.admin_order_field = 'section__name'
    
    list_display = ['order', 'name', 'org', 'location', 'startdate', 'enddate',
        'getSection']
    
class DetailAdminInline(admin.StackedInline):
    model = models.Detail
    extra = 0
    exclude = ['img_width', 'img_height']
    
class ProjectAdmin(SlugAdmin, RichTextAdmin, ReorderAdmin):
    list_display = ['order', 'name', 'completion_date', 'role', _summary]
    exclude = ['img_width', 'img_height']
    inlines = [DetailAdminInline]


admin.site.register(models.ResumeHeader, HeaderAdmin)
admin.site.register(models.ResumeSection, SectionAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Project, ProjectAdmin)