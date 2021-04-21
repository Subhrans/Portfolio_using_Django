from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import (MyDetail,
                     Project,
                     Achievment,
                     Social_Site_Connection,
                     Subscribe,
                     ContactUs,
                     MailBackend,
                     Language,
                     Service,

                     )

# Register your models here.

admin.site.unregister(User)


# class URLInline(admin.StackedInline):
#     model = URL
#
#
# admin.site.register(URL)


@admin.register(User)
class UserModifiedAdmin(UserAdmin):
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        if request.user.is_superuser:
            important_dates = ('last_login', 'date_joined')
            permissions = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            permissions_text = "Permissions"
            # readonly_fields = ('username', 'last_login', 'date_joined')

        else:
            important_dates = ('last_login', 'date_joined')
            permissions = ()
            permissions_text = None
            # readonly_fields = ('username', 'last_login', 'date_joined')
        return [(None, {
            'fields': ('username', 'password'),
        }),
                ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
                (permissions_text, {
                    'fields': permissions,
                }),
                ('Important dates', {'fields': important_dates}), ]

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            readonly_fields = ()
        else:
            readonly_fields = ('username', 'last_login', 'email', 'date_joined')
        return readonly_fields

    def get_queryset(self, request):
        qs = super(UserModifiedAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user.username)

    # inlines = (URLInline,)


@admin.register(MyDetail)
class MyDetailAdmin(admin.ModelAdmin):
    # fields = ['id','url']
    list_display = ['id', 'user', 'slug', 'url', 'visited']
    list_display_links = ['id', 'user', 'slug']

    # list_editable = ['visited']

    # prepopulated_fields = {"url":('id',)}
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(self, MyDetailAdmin).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(MyDetailAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "projects_detail":
            kwargs["queryset"] = Project.objects.filter(user=request.user)
        if db_field.name == "services":
            kwargs["queryset"] = Service.objects.filter(user=request.user)
        return super(self, MyDetailAdmin).formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "social_site_connection_details":
            kwargs['queryset'] = Social_Site_Connection.objects.filter(user=request.user)
        if db_field.name == "achievement_details":
            kwargs['queryset'] = Achievment.objects.filter(user=request.user)
        return super(self, MyDetailAdmin).formfield_for_foreignkey(db_field, request, **kwargs)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'slug', 'user']
    list_display_links = ['name', 'id', 'slug', 'user']
    list_filter = ['language_used', 'created_date']
    search_fields = ('language_used__name', 'id', 'name', 'created_date', 'user__username', 'user__email')

    # prepopulated_fields = {"slug":('name','language_used','created_date')}
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(self, ProjectAdmin).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(ProjectAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(Project, ProjectAdmin)

admin.site.register(Language)


@admin.register(Achievment)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'event_name']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(self, AchievementAdmin).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(AchievementAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(self, SubscribeAdmin).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(SubscribeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Social_Site_Connection)
class SocialSiteConnectionAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(self, SocialSiteConnectionAdmin).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(SocialSiteConnectionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(self, ContactUsAdmin).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(ContactUsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(MailBackend)
class MailBackendAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(self, MailBackendAdmin).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(MailBackendAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['user', 'name']

    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count() >= 4:
            self.message_user(request, 'Only four entries can exist at once - please remove others first',
                              messages.ERROR)
            return HttpResponseRedirect("/admin/Portfolio/service/")
        return super(self, ServiceAdmin).add_view(request, form_url, extra_context)

    def get_queryset(self, request):
        qs = super(ServiceAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ServiceAdmin, self).save_model(request, obj, form, change)
