from django.urls import path
from django.conf.urls import url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import *


schema_view = get_schema_view(
    openapi.Info(
        title="Questionnaire API",
        default_version='v1',
        description="Test API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vacantionit@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('auth/', AuthView.as_view()),
    path('create_questionnaire/', QuestionnaireCreateView.as_view()),
    path('list_active_questionnaire/', QuestionnaireActiveListView.as_view()),
    path('update_questionnaire/<int:pk>', QuestionnaireUpdateView.as_view()),
    path('delete_questionnaire/<int:pk>', QuestionnaireDeleteView.as_view()),

    path('create_question/', QuestionCreateView.as_view()),
    path('update_question/<int:pk>', QuestionUpdateView.as_view()),
    path('delete_question/<int:pk>', QuestionDeleteView.as_view()),

    path('create_answer/', AnswerCreateView.as_view()),
    path('result_questionnaire/<int:pk>', ResultQuestionnaireListView.as_view()),

]
