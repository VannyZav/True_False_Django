from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path
from api.views import ProductModelViewSet, UserModelViewSet, CheckProductView, ApiUserModelViewSet

router = DefaultRouter()
# router.register('api_users', ApiUserModelViewSet) не нужный роутер, на всякий случай пока остается
router.register('product', ProductModelViewSet)
router.register('users', UserModelViewSet)

urlpatterns = [
    path('check-product/', CheckProductView.as_view(), name='check_product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.extend(router.urls)
