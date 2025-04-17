from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Elliot Alderson', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='Dade Murphy', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(*users[:3])
        team2.members.add(*users[3:])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], description='Cycling for 1 hour'),
            Activity(_id=ObjectId(), user=users[1], description='Crossfit for 2 hours'),
            Activity(_id=ObjectId(), user=users[2], description='Running for 1.5 hours'),
            Activity(_id=ObjectId(), user=users[3], description='Strength training for 30 minutes'),
            Activity(_id=ObjectId(), user=users[4], description='Swimming for 1.25 hours'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team1, score=100),
            Leaderboard(_id=ObjectId(), team=team2, score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', duration=60),
            Workout(_id=ObjectId(), name='Crossfit', duration=120),
            Workout(_id=ObjectId(), name='Running Training', duration=90),
            Workout(_id=ObjectId(), name='Strength Training', duration=30),
            Workout(_id=ObjectId(), name='Swimming Training', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
