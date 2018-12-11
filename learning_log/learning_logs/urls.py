"""Define URL patterns for learning_logs."""


from django.urls import path

from . import views


urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Show all topics.
    path('topics/', views.topics, name='topics'),
    path(r'topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path(r'new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path(r'edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
