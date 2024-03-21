from rest_framework.routers import DefaultRouter

from api.views import ApiUserModelViewSet, ProductModelViewSet, UserModelViewSet

router = DefaultRouter()
router.register('api_users', ApiUserModelViewSet)
router.register('product', ProductModelViewSet)
router.register('users', UserModelViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
