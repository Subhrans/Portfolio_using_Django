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
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        if request.user.is_superuser:
            important_dates = ('last_login', 'date_joined')
            # readonly_fields = ('username', 'last_login', 'date_joined')
        else:
            important_dates = ('last_login', 'date_joined')
            # readonly_fields = ('username', 'last_login', 'date_joined')
        return [(None, {
                'fields': ('username', 'password'),
            }),
            ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
                ('Permissions', {
                    'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
                }),
                ('Important dates', {'fields': important_dates}), ]

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            readonly_fields = ()
            return readonly_fields
        else:
            readonly_fields = ('username', 'last_login','email', 'date_joined')
            return readonly_fields
        # fieldsets = (
        #     (None, {
        #         'fields': ('username', 'password'),
        #     }),
        #     ('important dates', {
        #         'fields': ('last_login', 'date_joined'),
        #     })
        # )
        # readonly_fields = ('username','last_login','date_joined')

    def get_queryset(self, request):
        qs = super(UserModifiedAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user.username)


@admin.register(MyDetail)
class MyDetailAdmin(admin.ModelAdmin):
    # fields = ['id','url']
    list_display = ['id', 'user', 'slug', 'url']
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

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "projects_detail":
            kwargs["queryset"] = Project.objects.filter(user=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "social_site_connection_details":
            kwargs['queryset'] = Social_Site_Connection.objects.filter(user=request.user)
        if db_field.name == "achievment_details":
            kwargs['queryset'] = Achievment.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


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
