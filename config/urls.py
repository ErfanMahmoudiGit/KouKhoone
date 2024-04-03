from django.contrib import admin
from django.urls import path, include
#from rest_framework.authtoken.views import obtain_auth_token
#from api.views import RevokeToken
#from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ("blog.urls")),
    path('api/', include('api.urls')),

    #the following path is not needed. because i no longer use session for auth.
    #path('api-auth/', include('rest_framework.urls')),

    #the following path is not needed. because i no longer use token for auth.
    #path('api/token-auth/', obtain_auth_token),
    #path ('api/revoke/', RevokeToken.as_view()),

    #path('api/rest-auth/', include('dj_rest_auth.urls')),
    #path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    #path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# the following 3 lines are used to fix the bug while trying to see the images in debug mode.
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
