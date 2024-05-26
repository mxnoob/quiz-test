from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from .views import AnswerViewSet, GameViewSet, QuestionViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('games', GameViewSet, basename='games')
router_v1.register(
    r'games/(?P<game_id>\d+)', QuestionViewSet, basename='questions'
)
router_v1.register(
    r'games/(?P<game_id>\d+)/questions/(?P<question_id>\d+)',
    AnswerViewSet,
    basename='answers',
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(
        'docs/',
        include_docs_urls(title='Quiz API Documentation'),
        name='api-docs',
    ),
]
