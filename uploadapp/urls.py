from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
   # path('', FileUploadView.as_view()),
    path('data/', DataList.as_view()),
    path('data/<int:pk>', DataDetail.as_view())
    # url(r'^.*', TemplateView.as_view(template_name="index.html"), name="index")

]

urlpatterns = format_suffix_patterns(urlpatterns)