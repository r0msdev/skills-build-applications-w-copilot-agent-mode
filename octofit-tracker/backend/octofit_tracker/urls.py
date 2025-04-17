"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

# Define API root and routers
router = DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/teams', views.TeamViewSet)
router.register(r'api/activities', views.ActivityViewSet)
router.register(r'api/leaderboard', views.LeaderboardViewSet)
router.register(r'api/workouts', views.WorkoutViewSet)

urlpatterns = [
    path('', views.api_root, name='api-root'),  # Set api_root as the root view
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
