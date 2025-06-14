from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    ded_line = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tags')

    class Meta:
        ordering = ["done", '-datetime']

    def __str__(self):
        task_tags = self.tags.all()

        tag_names = ", ".join([tag.name for tag in task_tags])
        return f"{self.content}: {tag_names} ({self.done})"
