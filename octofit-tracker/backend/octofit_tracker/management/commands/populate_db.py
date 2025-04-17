from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create Users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', password='password123')
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', password='password123')

        # Create Teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1)
        team1.members.add(user2)

        # Create Activities
        Activity.objects.create(user=user1, description='Running 5km', date='2025-04-15T10:00:00Z')
        Activity.objects.create(user=user2, description='Cycling 10km', date='2025-04-16T15:00:00Z')

        # Create Leaderboard
        Leaderboard.objects.create(team=team1, score=100)

        # Create Workouts
        Workout.objects.create(name='Morning Yoga', duration=30)
        Workout.objects.create(name='Evening Cardio', duration=45)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
