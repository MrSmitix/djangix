from django.contrib import admin


class ReadOnlyModelAdmin(admin.ModelAdmin):
    """ Базовая read-only админка """

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ReadOnlyTabularInlineAdmin(admin.TabularInline):
    """ Базовая tabular read-only админка """

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ReadOnlyStackedInlineAdmin(admin.StackedInline):
    """ Базовая tabular read-only админка """

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


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
