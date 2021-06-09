from django.conf.urls import include, url
from rest_framework import routers

from api.views.AuthorsViewset import AuthorViewSet
from api.views.ArticlesViewset import ArticleViewSet
from api.views.SignUpViewset import SignupViewset
from api.views.LoginViewset import LoginViewset
from api.views.ArticlesListViewset import ArticleListViewSet

router = routers.DefaultRouter()
router.register(r'admin/authors', AuthorViewSet)
router.register(r'admin/articles', ArticleViewSet)
router.register(r'signup', SignupViewset)
router.register(r'articles', ArticleListViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'login', LoginViewset.as_view()),
]
