from background_task import background
from django.contrib.auth.models import User
from celery.decorators import task
from celery.utils.log import get_task_logger

@background(schedule=60)
def notify_user(user_id):
    # lookup user by id and send them a message
    user = User.objects.get(pk=user_id)
    user.email_user('Here is a notification', 'You have been notified')
    notify_user(user.id)


logger = get_task_logger(__name__)

@task
def set_race_as_inactive(race_object):
    race_object.is_active = False # set the race as not active 
    race_object.save() # save the race object 