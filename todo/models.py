from django.db import models

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class ToDo(models.Model):
    position = models.IntegerField(default=0)
    name = models.CharField(max_length=60)
    date_create = models.DateField(auto_now_add=True)
    priority = models.ForeignKey(
        'Priority',
        null=True,
        on_delete=models.SET_NULL,
        related_name='todos'
    )
    status = models.CharField(max_length=10, default='In process')

    def __str__(self):
        return f'{self.pk} - {self.position} - {self.name} - ' \
               f'{self.date_create} - {self.priority.name} - {self.status}'
