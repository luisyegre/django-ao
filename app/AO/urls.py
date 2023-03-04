from django.urls import path
from .views import *
#router = routers.DefaultRouter()
#router.register(r'appoinments',AppoinmentView)

urlpatterns = [
    # path('appoinments/<int:pk>',get_one_appoinment),
    # path('appoinments/',get_all_appoinments),
    # path('appoinments/',register_appoinment),
    path('appoinments/<int:appo_pk>',AppoinmentView.as_view()),
    path('appoinments/',AppoinmentView.as_view()),
    path('organization/<int:org_pk>/appoinments/<int:appo_pk>',AppoinmentView.as_view()),
    path('organization/<int:org_pk>/appoinments/',AppoinmentView.as_view())
]