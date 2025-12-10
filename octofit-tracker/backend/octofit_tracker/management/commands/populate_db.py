from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Usuń istniejące dane
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Dodaj drużyny
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Dodaj użytkowników
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True),
        ]

        # Dodaj aktywności
        Activity.objects.create(user='Iron Man', type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user='Captain America', type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user='Batman', type='Swimming', duration=25, date=timezone.now().date())
        Activity.objects.create(user='Wonder Woman', type='Yoga', duration=60, date=timezone.now().date())

        # Dodaj leaderboard
        Leaderboard.objects.create(team='Marvel', points=150)
        Leaderboard.objects.create(team='DC', points=120)

        # Dodaj treningi
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='HIIT', description='High intensity interval training', difficulty='Hard')
        Workout.objects.create(name='Yoga Flow', description='30 min yoga session', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('Baza octofit_db została wypełniona przykładowymi danymi.'))
