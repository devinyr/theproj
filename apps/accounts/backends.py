from django.conf import settings
from django.contrib.auth.hashers import check_password
from apps.accounts.models import User

class EmailAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """

    def authenticate(self, email=None, password=None):
        """
        Authentication method
        """
        try:
            print "Authen Email"
            print email
            user = User.objects.get(email=email)
            print password
            print user
            print "To check"
            print user.password
            if check_password(password, user.password):
                print "check_password"
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None