from django.urls import path
from questlog import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('quests/', views.QuestlogList.as_view()),
    path('quests/<int:pk>/', views.QuestlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)