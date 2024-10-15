from rest_framework import viewsets
from .models import Testimonio
from .serializers import TestimonioSerializer

class TestimonioViewSet(viewsets.ModelViewSet):
    queryset = Testimonio.objects.all()
    serializer_class = TestimonioSerializer



# Create your views here.
