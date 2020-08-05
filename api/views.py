from datetime import datetime
from rest_framework import viewsets
from order.models import User
from .serializers import UserSerializer


class AllUsersView(viewsets.ModelViewSet):
    """
    API endpoint that allows all users to be viewed
    """
    queryset = User.objects.select_related('order').all()
    serializer_class = UserSerializer


class DateUsersView(viewsets.ModelViewSet):
    """
    API endpoint that allows you to view users filtered by registration date
    """
    url_arg = "registration_date"
    serializer_class = UserSerializer

    def get_queryset(self):
        date_str = self.kwargs.get(self.url_arg)
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            qs = User.objects.select_related('order').filter(registration_date=date)
            return qs
        except ValueError:
            return []
