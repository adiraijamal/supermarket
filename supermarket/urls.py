from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('customers/', include('customers.urls', namespace='customers')),
    path('vendors/', include('vendors.urls', namespace='vendors')),
    path('products/', include('products.urls', namespace='products')),
    path('purchase/', include('purchases.urls', namespace='purchase')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
