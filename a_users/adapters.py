from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_signup_redirect_url(self, request):
        """
        Returns the URL to redirect to after a successful signup.
        """
        return resolve_url('profile-onboarding')