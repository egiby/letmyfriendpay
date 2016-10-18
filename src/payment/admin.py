from django.contrib import admin

from .models import Payment


class MemberInline(admin.TabularInline):
    model = Payment.members.through


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    exclude = ('members',)
    inlines = (MemberInline,)

admin.site.register(Payment, PaymentAdmin)
