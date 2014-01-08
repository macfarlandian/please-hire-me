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
    jobs = models.Job.objects.all()
    schools = models.School.objects.all
    skillareas = models.SkillArea.objects.all
    awards = models.Award.objects.all
    return render_to_response('portfolio/resume.html', 
        {'jobs' : jobs, 'schools': schools, 'skillareas': skillareas, 'awards': awards},
        RequestContext(request))
    