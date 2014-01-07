from django.contrib import admin
from . import models

class RichTextAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    class Media:
        js = [
                '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/static/grappelli/tinymce_setup/tinymce_setup.js',
            ]

admin.site.register(models.ResumeHeader, RichTextAdmin)
admin.site.register(models.ResumeSection, RichTextAdmin)
admin.site.register(models.Role, RichTextAdmin)
admin.site.register(models.Project, RichTextAdmin)
admin.site.register(models.Detail, RichTextAdmin)