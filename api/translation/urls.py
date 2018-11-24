from django.urls import path
from .views import TranslationsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('translations', TranslationsView, base_name='Translations')

urlpatterns = router.urls
#     # path('translations', ListCreateTranslationsView.as_view(), name="translations-list-create"),
#     # path('translations/<int:pk>', RetrieveUpdateDestroyTranslationsView.as_view(), name="translations-detail")


