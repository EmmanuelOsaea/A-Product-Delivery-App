const stripe = Stripe(' ');

const {error, paymentIntent} = await stripe.confirmCardPayment(clientSecret, {
  payment_method: {
    card: cardElement,
    billing_details: {
      name: 'Client Name',
    },
  }
});
if (error) {
  console.error(error.message);
} else {
  console.log('Payment Done!');
  }
