# all the imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm
import models

# your name, from header, for all views
def getname():
    name = {}
    header = models.ResumeHeader.objects.get(pk=1)
    name['first'] = header.first_name
    name['last'] = header.last_name
    name['photo'] = header.photo
    name['w'] = header.img_width
    name['h'] = header.img_height
    return name

def portfolio(request):
    project_list = models.Project.objects.all()
    return render_to_response('portfolio/portfolio.html', 
        {'project_list' : project_list, 'name': getname() }, RequestContext(request))

def project(request, slug):
    project = models.Project.objects.get(slug=slug)
    return render_to_response('portfolio/project.html', 
        {'project': project, 'name': getname() }, RequestContext(request))

def role(request, slug):
    role = models.Role.objects.get(slug=slug)
    return render_to_response('portfolio/role.html', 
        {'role': role, 'name': getname() }, RequestContext(request))

def resume(request):
    return render_to_response('portfolio/resume.html', 
    {'header': header, 'name': getname() }, RequestContext(request))
    