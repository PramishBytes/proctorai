from django.contrib.admin import AdminSite
from django.utils.html import format_html
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student, CheatingEvent, Exam, CheatingImage, CheatingAudio
from django.contrib import admin


# Custom Admin Site
class MyAdminSite(AdminSite):
    site_header = 'MyProctor Admin'
    site_title = 'MyProctor Portal'
    index_title = 'Welcome Admin'

    def index(self, request, extra_context=None):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (reverse('admin:login'), request.path))
        return render(request, 'admin_dashboard.html')


# Create instance of custom admin site
my_admin_site = MyAdminSite(name='myadmin')


# Student model customization
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp', 'feedback', 'photo_tag')
    search_fields = ('name', 'email')
    list_filter = ('timestamp',)

    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" alt="Photo">', obj.photo.url)
        return "No Photo"

    photo_tag.short_description = 'Photo'


# Registering models with the custom admin site
my_admin_site.register(Student, StudentAdmin)
my_admin_site.register(CheatingEvent)
my_admin_site.register(Exam)
my_admin_site.register(CheatingImage)
my_admin_site.register(CheatingAudio)
