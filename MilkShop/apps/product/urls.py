from django.urls.conf import path
from .views import ProductList, ProductReviewList


urlpatterns = [
    path('', ProductList.as_view(), name='product'),
    path('product_review/', ProductReviewList.as_view(), name='product'),
    # path('api/users/registration', UserList.as_view(), name='users/registration'),
]