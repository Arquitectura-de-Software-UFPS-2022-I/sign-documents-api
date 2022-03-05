from rest_framework import routers
from django.urls import path
from .api import AuthenticationViewSet, FileViewSet, ListSignatureRequestByUserViewSet, ListSignatureRequestUserByRequestViewSet, ListSignatureRequestUserByUserViewSet, SignatureRequestUserViewSet, SignatureRequestViewSet, UserViewSet, GetGenerateFileSignedFromRequestSignature

router = routers.DefaultRouter()
router.register('files', FileViewSet, 'files')
router.register('users', UserViewSet, 'users')
router.register('signature_requests', SignatureRequestViewSet, 'signature requests')
router.register('signature_request_users', SignatureRequestUserViewSet, 'signature request users')

urlpatterns = router.urls

urlpatterns += [
    path('auth/user/', AuthenticationViewSet.as_view(), name='authentication for user'),
    path('signature_requests_by_user/<int:user_id>/', ListSignatureRequestByUserViewSet.as_view(), name='signature requests by user'),
    path('signature_request_users_by_user/<int:user_id>/', ListSignatureRequestUserByUserViewSet.as_view(), name='signature requests users by user id'),
    path('signature_request_users_by_request/<int:request_id>/', ListSignatureRequestUserByRequestViewSet.as_view(), name='signature requests users by request id'),
    path('generate_pdf/<int:request_id>/', GetGenerateFileSignedFromRequestSignature.as_view(), name='generate file signed by request id'),
]
