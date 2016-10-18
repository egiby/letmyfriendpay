from django.contrib import admin

from .models import Wallet


class WalletMemberInline(admin.TabularInline):
    model = Wallet.members.through


class WalletAdmin(admin.ModelAdmin):
    model = Wallet
    exclude = ('members',)
    inlines = (WalletMemberInline,)

admin.site.register(Wallet, WalletAdmin)
