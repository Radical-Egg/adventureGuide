from questlog.models import Questlog
from questlog.serializers import QuestlogSerializer
from rest_framework import generics


class QuestlogList(generics.ListCreateAPIView):
    queryset = Questlog.objects.all()
    serializer_class = QuestlogSerializer

class QuestlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questlog.objects.all()
    serializer_class = QuestlogSerializer





    
