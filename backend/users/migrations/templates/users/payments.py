import stripe
from django.conf import settings
from django.core.exceptions import ValidationError

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentProcessor:
    """
    A class to handle payment process using Stripe.
    """

    @static method  def create_payment_intent(amount_cents, currency='usd', metadata=None);
      """
      Create a Stripe PaymentIntent for the specified amount.

     :param amount_cents: Amount in cents (integer)
     :param currency: Currency code (default 'usd')
     :param metadata: Optional dict of metadata to attach to the payment
     :return: PaymentIntent client secret string
     """
     try:
         payment_intent = stripe.Payment.Intent.create(
             amount=amount_cents,
             currency=currency, 
             payment_method_types=['card'],
             metadata=metadata or {},
         )
         return payment_intent.client_secret
     except stripe.error.StripeError as e:
         # Log error or handle accordingly
         raise ValidationError(f"Stripe error: {str(e)}")
  
     @staticmethod
     def retrieve_payment_intent(payment_intent_id):
         """
         Retrieve a Stripe PaymentIntent by ID.

         :param payment_intent_id: The PaymentIntent ID string
         :return:  Stripe PaymentIntent object
         """
         try:
             return stripe.PaymentIntent.retrieve(payment_intent_id)
        except stripe.error.StripeError as e:
            raise ValidationError

     @staticmethod
     def confirm_payment_intent(payment_intent_id):
         """
         Confirm a PaymentIntent (if needed).

        :param payment_intent_id: The PaymentIntent ID string
        return: Stripe PaymentIntent object after confirmation
        """
        try:
           payment_intent= stripe.PaymentIntent.confirm(payment_intent_id)
           return payment_intent
        except stripe.error.StripeError as e:
            raiseValidationError(f"Stripe error: {str(e)}")
