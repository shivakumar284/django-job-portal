from django.db import models
from django.contrib .auth.models import User
# Create your models here.
class Job(models.Model):
  title=models.CharField(max_length=200)
  company=models.CharField(max_length=200)
  location=models.CharField(max_length=200)
  description=models.TextField()
  posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.title}-{self.company}"
  
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"