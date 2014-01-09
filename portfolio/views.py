# all the imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm
import models

# your name, from header, for all views
name = {}
header = models.ResumeHeader.objects.get(pk=1)
name['first'] = header.first_name
name['last'] = header.last_name

def portfolio(request):
    project_list = models.Project.objects.all()
    return render_to_response('portfolio/portfolio.html', 
        {'project_list' : project_list, 'name': name }, RequestContext(request))

def project(request, slug):
    project = models.Project.objects.get(slug=slug)
    return render_to_response('portfolio/project.html', 
        {'project': project, 'name': name }, RequestContext(request))

def role(request, slug):
    role = models.Role.objects.get(slug=slug)
    return render_to_response('portfolio/role.html', 
        {'role': role, 'name': name }, RequestContext(request))

def resume(request):
    return render_to_response('portfolio/resume.html', 
    {'header': header, 'name': name }, RequestContext(request))
    