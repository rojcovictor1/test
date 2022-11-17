from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from rest_framework import routers

from products.views import ProductsAPIView
from products.views import PostProductAPIView

router = routers.DefaultRouter()
router.register(r'products', ProductsAPIView)

post_product = PostProductAPIView.as_view({'post': 'create'})

urlpatterns = [
                  path('', post_product, name='create_product'),
                  path('', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('api/', include('rest_framework.urls', namespace='rest_framework'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
