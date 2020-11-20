from rest_framework import serializers
from questlog.models import Questlog

class QuestlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questlog
        fields = ['id', 'questTitle', 'questContent']