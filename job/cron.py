from django_cron import CronJobBase, Schedule
from .models import Job, Student, Revenue, College, DegreeStream, DiplomaStream, MasterDegreeStream
from django.core.management import BaseCommand

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        print("helo")    # do your thing here


# class MyCronJob(CronJobBase):
#     def handle(self, **options):
#         today = timezone.now().date()
#         for user in Student.objects.filter(birth_date__day=today.day, birth_date__month=today.month):
#             subject = 'Happy birthday %s!' % user.sname
#             body = 'Hi %s,\n...' + user.sname
#             send_mail(subject, body, 'r.poornimashetty@gmail.com', [user.semail])