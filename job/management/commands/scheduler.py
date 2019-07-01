from django.core.management.base import BaseCommand, CommandError
from .models import Job

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('sid', nargs='+', type=int)

    def handle(self, *args, **options):
        for sid in options['sid']:
            try:
                job = Job.objects.get(pk=sid)
            except Job.DoesNotExist:
                raise CommandError('Job "%s" does not exist' % sid)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % sid))