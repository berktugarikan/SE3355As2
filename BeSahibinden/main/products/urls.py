from django.urls import path
from .views import getAllProducts, getDetail, search_product
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', getAllProducts.as_view(), name='retrieve-all-products'),
    path('<int:product_id>/', getDetail.as_view(), name='product-detail'),
    path('search/', search_product.as_view(), name='search-product'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
