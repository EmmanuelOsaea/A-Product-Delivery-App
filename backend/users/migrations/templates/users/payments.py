import stripe
from django.conf import settings
from django.core.exceptions import ValidationError

stripe.api_key = settings.STRIPE_SECRET_KEY
