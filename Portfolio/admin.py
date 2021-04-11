from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import (MyDetail,
                     Project,
                     Achievment,
                     Social_Site_Connection,
                     Subscribe,
                     ContactUs,
                     MailBackend,
                     Language,
                     )

# Register your models here.
admin.site.unregister(User)


@admin.register(User)
class UserModifiedAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super(UserModifiedAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user.username)


@admin.register(MyDetail)
class MyDetailAdmin(admin.ModelAdmin):
    # fields = ['id','url']
    list_display = ['id', 'url', 'user', 'slug']
    list_display_links = ['id', 'user', 'slug']

    # prepopulated_fields = {"url":('id',)}
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(MyDetailAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'slug', 'user']
    list_display_links = ['name', 'id', 'slug', 'user']

    # prepopulated_fields = {"slug":('name','language_used','created_date')}
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(ProjectAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(Project, ProjectAdmin)

admin.site.register(Language)


@admin.register(Achievment)
class AcievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'event_name']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(AcievementAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(SubscribeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Social_Site_Connection)
class Social_Site_ConnectionAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(Social_Site_ConnectionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(ContactUsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(MailBackend)
class MailBackend(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(MailBackend, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
