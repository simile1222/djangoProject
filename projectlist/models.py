from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def average_rating(self):
        ratings = self.ratings.all()
        return round(sum(r.score for r in ratings)/ratings.count(),2) if ratings.exists() else 0
    def get_rank(self):
        all_projects = Project.objects.all().annotate(avg=models.Avg('ratings__score'))
        all_projects = sorted(all_projects, key=lambda p: p.avg or 0, reverse=True)
    
        for idx, project in enumerate(all_projects, start=1):
            if project.id == self.id:
                return idx
        return None

    
class Rating(models.Model):
    project = models.ForeignKey(Project, related_name='ratings', on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, f'{i}점') for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)