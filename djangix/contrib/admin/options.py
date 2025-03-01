from django.contrib import admin


class ReadOnlyModelMixin:
    """ Базовая read-only админка """

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ReadOnlyModelAdmin(admin.ModelAdmin, ReadOnlyModelMixin):
    """ Базовая read-only админка """


class ReadOnlyTabularInlineAdmin(admin.ModelAdmin, ReadOnlyModelMixin):
    """ Базовая read-only админка """


class BaseAppModelAdmin(admin.ModelAdmin):
    """ Базовая админка для приложений """

    list_display = ('id', 'app_name_display', 'app')
    list_display_links = ('app',)

    readonly_fields = ('app',)

    search_fields = ('app',)

    @admin.display(description='Название')
    def app_name_display(self, obj):
        return obj.get_app().label

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
