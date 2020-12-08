"""lzkshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include,re_path
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from django.views.static import serve

from lzkshop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from trade.views import ShoppingCartViewset, OrderViewset
from user_operation.views import UserFavViewSet, LeavingMessageViewset, AddressViewset
from users.views import SmsCodeViewset,UserViewset

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet,basename='goods')
# 配置Category的url
router.register(r"categorys", CategoryViewSet, basename="categorys")
# 配置codes的url
router.register(r'code', SmsCodeViewset, basename="code")
# 配置注册的url
router.register(r"users",UserViewset,basename="users")
# 配置用户收藏的url
router.register(r"userfavs",UserFavViewSet,basename="userfavs")
# 配置用户留言的url
router.register(r"messages",LeavingMessageViewset, basename="messages")
# 配置收货地址
router.register(r"address",AddressViewset,basename="address")
# 配置购物车的url
router.register(r"shopcarts",ShoppingCartViewset,basename="shopcarts")
# 配置订单的url
router.register(r"orders",OrderViewset,basename="orders")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path("ueditor/",include("DjangoUeditor.urls")),
    # drf文档，title自定义
    path("docs",include_docs_urls(title="北风向南")),
    path('api-auth/', include('rest_framework.urls')),


    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # 商品列表页
    # path("goods/",GoodsListView.as_view(),name="goods-list"),
    re_path('^', include(router.urls)),
    # token
    path('api-token-auth/',views.obtain_auth_token),
    # jwt的token认证接口
    path('jwt-auth/', obtain_jwt_token),
    # jwt的认证接口
    path("login/",obtain_jwt_token),


]
