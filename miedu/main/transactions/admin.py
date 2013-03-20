from django.contrib import admin
from transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    readonly_fields = ("last_viewed", "transaction_date")
    fieldsets = (
        (None, {'fields': ( 
        			('account', 'active', 'completed', 'consummated'),
                    ('transaction_date', 'start_date', 'expiration_date'),
                    ('last_viewed', 'relationship'),
                    ('campaign', 'amount_supported'),
                    )
                }
        ),
    )

admin.site.register(Transaction, TransactionAdmin)