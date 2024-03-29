"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('volunteer.urls')),
    # path('accounts/', include('allauth.urls')),
#    path('login_user/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('volunteer/', include('volunteer.urls')),

]


# urlpatterns = [
#     path( 'browse_roster/<str:year2view>/', views.browse_roster, name='browse_roster' ),
#     path( 'csv/<str:year2view>/', views.csv, name='csv' ),
#     # path( 'formset_practice/<int:membership_id>/', ModelFormWizard.as_view([CreateMembershipEntry, MemberShipYearsForm], membership_id='membership_id'), name='formset_practice'),
#     path( 'entry_form/<membership_id>/', views.entry_form, name='entry_form'),
#     path( 'create/', views.create, name='create'),
#     path( 'update/<int:member_id>/<str:year2view>/', views.update, name='update' ),
#     path( 'mailtest/', views.mailtest, name='mailtest' ),
#     #  path( '', views.front_page, name='home' ),
#     path( '', TemplateView.as_view(template_name='front_page.html'), name='home'),
#     ]