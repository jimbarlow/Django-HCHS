from django.contrib import admin

# Register your models here.
from volunteer.models import Volunteers
from django import forms
from ckeditor.widgets import CKEditorWidget

from django.contrib import admin

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)

admin.site.register(Volunteers)


