from bson import ObjectId
from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    members = UserSerializer(many=True) # Serialize the user field as a nested User object

    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = UserSerializer()  # Serialize the user field as a nested User object

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'description', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    team = TeamSerializer()  # Serialize the team field as a nested Team object

    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'score']

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = Workout
        fields = '__all__'