# all the imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm
import models

def portfolio(request):
    project_list = models.Project.objects.all()
    return render_to_response('portfolio/portfolio.html', 
        {'project_list' : project_list}, RequestContext(request))

def project(request, slug):
    project = models.Project.objects.get(slug=slug)
    return render_to_response('portfolio/project.html', 
        {'project' : project}, RequestContext(request))

def role(request, slug):
    role = models.Role.objects.get(slug=slug)
    return render_to_response('portfolio/role.html', 
        {'role' : role}, RequestContext(request))

def resume(request):
    content = {'header' : models.ResumeHeader.objects.get(pk=1)}
    return render_to_response('portfolio/resume.html', content, 
        RequestContext(request))
    