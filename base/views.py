from django.shortcuts import render
from .models import About, Job, Skill, Achievement, Item




def home(request):
    info =  About.objects.first()
    all_jobs = Job.objects.all()
    all_skills = Skill.objects.all()
    have = all_skills.count() / 2
    skills1 = all_skills[0:have]
    skills2 = all_skills[have:]
    achievements = Achievement.objects.all()
    videos = Item.objects.all()
    return render(request,'base/index.html', 
    {'info': info,
     'all_jobs':all_jobs, 
     'skills1':skills1, 
     'skills2':skills2, 
     'achievements': achievements, 
     'videos': videos})
