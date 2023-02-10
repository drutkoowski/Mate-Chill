from django.contrib import admin
from accounts.models import Account

from django.forms import ModelForm, PasswordInput


class AccountAdminForm(ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
        widgets = {
            'password': PasswordInput(render_value=True),
        }


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm


admin.site.register(Account, AccountAdmin)
