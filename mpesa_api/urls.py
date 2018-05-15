from django.conf.urls import include, patterns, url

from mpesa_api.views import B2cResult, B2cTimeOut, C2bConfirmation, C2bValidation, OnlineCheckoutCallback

app_name = 'mpesa'   

urlpatterns = [
    url('b2c/timeout/', B2cTimeOut.as_view(), name='b2c_timeout'),
    url('b2c/result/', B2cResult.as_view(), name='b2c_result'),
    url('c2b/confirmation/', C2bConfirmation.as_view(), name='c2b_confirmation'),
    url('c2b/validate/', C2bValidation.as_view(), name='c2b_validation'),
    url('c2b/online_checkout/callback/', OnlineCheckoutCallback.as_view(), name='c2b_checkout_callback'),
    url('payment/', Order.as_view(), name='mpesa_payment'),
]
