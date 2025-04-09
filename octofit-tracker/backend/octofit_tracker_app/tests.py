from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="test@example.com", name="Test User", age=25)

    def test_user_creation(self):
        user = User.objects.get(email="test@example.com")
        self.assertEqual(user.name, "Test User")

# Add similar test cases for Team, Activity, Leaderboard, and Workout
    def test_team_creation(self):   
        team = Team.objects.create(name="Test Team", members=["user1", "user2"])
        self.assertEqual(team.name, "Test Team")
        self.assertEqual(team.members, ["user1", "user2"])
    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, activity_type="Running", duration=30)
        self.assertEqual(activity.activity_type, "Running")
        self.assertEqual(activity.duration, 30)
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user=self.user, score=100)
        self.assertEqual(leaderboard.score, 100)
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Test Workout", description="This is a test workout.")
        self.assertEqual(workout.name, "Test Workout")
        self.assertEqual(workout.description, "This is a test workout.")
    def test_user_update(self):
        self.user.name = "Updated User"
        self.user.save()
