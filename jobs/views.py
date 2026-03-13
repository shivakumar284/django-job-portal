from django.shortcuts import render ,get_object_or_404,redirect
from .models import Job,Application 

#from rest_framework import viewsets
#from .serializers import Applicationserializer
# Create your views here.
def job_list(request):
  jobs= Job.objects.all()
  return render(request,"jobs/job_list.html",{"jobs":jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    if request.method == "POST":
        cover_letter = request.POST.get("cover_letter")

        Application.objects.create(
            user=request.user,
            job=job,
            cover_letter=cover_letter
        )

        return redirect("job_list")

    return render(request, "jobs/apply_job.html", {"job": job})