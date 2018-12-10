"""Define URL patterns for learning_logs."""


from django.urls import path

from . import views


urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Show all topics.
    path('topics/', views.topics, name='topics'),
    path(r'topics/<int:topic_id>/', views.topic, name='topic'),
]
