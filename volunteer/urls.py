from django.urls import path, include, reverse
from . import views
# from .views import ModelFormWizard, about_us
# from .forms import VolunteerEntryForm
from django.views.generic import TemplateView

urlpatterns = [
    path( 'browse_roster/', views.browse_roster, name='browse_roster' ),
    # path( 'csv/<str:year2view>/', views.csv, name='csv' ),
    # # path( 'formset_practice/<int:membership_id>/', ModelFormWizard.as_view([CreateMembershipEntry, MemberShipYearsForm], membership_id='membership_id'), name='formset_practice'),
    # path( 'entry_form/<membership_id>/', views.entry_form, name='entry_form'),
    path( 'create/', views.create, name='create'),
    path( 'update/<int:volunteer_id>/', views.update, name='update' ),
    # path( 'mailtest/', views.mailtest, name='mailtest' ),
    #  path( '', views.front_page, name='home' ),
    path( '', TemplateView.as_view(template_name='front_page.html'), name='home'),
    # path("create/", CreateVolunteerEntry.as_view(), name='create'),
    path('ingest_tickets/', views.tickets, name='ingest_tickets'),
    path('print_roles_catalog/', views.print_roles_catalog, name='print_roles_catalog'),
    path('print_tickets/', views.print_tickets, name='print_tickets'),
    path('define_roles/', views.define_roles_catalog, name='define_roles'),
    path('update_roles_catalog/<int:role_id>/', views.update_roles_catalog, name='update_roles_catalog'),
    path('about_us/', views.about_us, name='about_us')
    ]