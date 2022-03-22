from django_celery_beat.models import PeriodicTask, CrontabSchedule


CrontabSchedule.objects.all().delete()
PeriodicTask.objects.all().delete()
schedule = CrontabSchedule.objects.create(minute='*/1')
task = PeriodicTask.objects.create(name='test1', task='apps.task.test1', crontab=schedule)
task.save()
