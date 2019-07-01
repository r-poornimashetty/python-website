from celery.utils.log import get_task_logger

@app.task
def set_race_as_inactive(race_object):
    """
    This celery task sets the 'is_active' flag of the race object 
    to False in the database after the race end time has elapsed.
    """

    race_object.is_active = False # set the race as not active 
    race_object.save() # save the race object 