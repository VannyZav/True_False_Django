from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('product', ProductModelViewSet)



urlpatterns = [

]

urlpatterns.extend(router.urls)