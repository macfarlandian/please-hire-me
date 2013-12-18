# all the imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm
import models

def home(request):
    project_list = models.Project.objects.all()
    return render_to_response('portfolio/home.html', 
        {'project_list' : project_list}, RequestContext(request))
    
def resume(request):
    jobs = models.Job.objects.all()
    schools = models.School.objects.all
    skillareas = models.SkillArea.objects.all
    awards = models.Award.objects.all
    return render_to_response('portfolio/resume.html', 
        {'jobs' : jobs, 'schools': schools, 'skillareas': skillareas, 'awards': awards},
        RequestContext(request))
    