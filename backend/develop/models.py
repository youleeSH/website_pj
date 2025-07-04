from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def average_score(self):
        scores = self.evaluation_set.all()
        if scores.exists():
            return round(sum(score.value for score in scores) / scores.count(), 2)
        return 0

    def __str__(self):
        return self.title

class Evaluation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.value}점"