from django import forms
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import Account, Education, Experience, Supporter, Organization
from campaigns.models import Campaign
from transactions.models import Transaction


class EducationInline(admin.TabularInline):
    model = Education
    max_num = 5
    extra = 1
    readonly_fields = (
    )

    fieldsets = (
        ('Educational Background', {
            'classes': ('collapse',),
            'fields': (
                'organization',
                'certification',
                'concentration',
                'courses',
                'notes',
                'grade',
                'start_date',
                'end_date',
            )                
        }),
    )

class ExperienceInline(admin.TabularInline):
    model = Experience
    max_num = 5
    extra = 1
    readonly_fields = (
    )

    fieldsets = (
        ('Work Experience', {
            'classes': ('collapse',),
            'fields': (
                'organization',
                'tasks',
                'notes',
                'start_date',
                'end_date',
            )                
        }),
    )

class SupporterInline(admin.TabularInline):
    model = Supporter
    max_num = 5
    fk_name = 'account'
    extra = 1
    readonly_fields = (
        'last_viewed',
    )

    fieldsets = (
        ('Supporters', {
            'classes': ('collapse',),
            'fields': (
                'supporter',
                'active',
                'completed',
                'start_date',
                'expiration_date',
                'last_viewed',
                'amount_supported',
                'campaign_field',
                'relationship',
            )                
        }),
    )

class CampaignInline(admin.TabularInline):
    model = Campaign
    max_num = 5
    extra = 1
    readonly_fields = (
    )

    fieldsets = (
        ('Campaigns', {
            'classes': ('collapse',),
            'fields': (
                'active',
                'title',
                'caption',
                'headline',
                'description',
                'endline',
                'summary',
                'call_to_action',
                'minimum_pledge',
                'goal',
                'city',
                'state',
                'country',
                'start_date',
                'end_date',
                'tags',
            )                
        }),
    )

class TransactionInline(admin.TabularInline):
    model = Transaction
    max_num = 5
    extra = 1
    readonly_fields = (
        'last_viewed',
        'transaction_date',
    )

    fieldsets = (
        ('Past Transactions', {
            'classes': ('collapse',),
            'fields': (
                'campaign',
                'active',
                'completed',
                'consummated',
                'transaction_date',
                'start_date',
                'expiration_date',
                'last_viewed',
                'amount_supported',
                'relationship',
            )                
        }),
    )

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    first_name = forms.CharField(label='FirstName', widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.CharField(label='Email/Username', widget=forms.TextInput(attrs={'placeholder':'Username/Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email',)
        widgets = { 'name': forms.TextInput(attrs={'class': "input-block-level"})}

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
            if commit:
                user.username = user.email
                user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AccountAdmin(UserAdmin):
    inlines = [EducationInline, ExperienceInline, SupporterInline, CampaignInline, TransactionInline]
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': (
                                ('first_name', 'last_name', 'email'),
                                ('date_of_birth', 'marital_status', 'kids'),
                                ('origin_country', 'origin_city'),
                                ('current_country', 'current_city'),
                                ('industry', 'function'),
                                'dp',
                                'objective',
                                'headline',
                                'unread'
                                )
                            }
        ),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),

    )

    list_display = UserAdmin.list_display + ('date_of_birth',)

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', 'js/libs/tiny_mce/tinymce_setup.js',)
        
# Now register the new UserAdmin...
admin.site.unregister(Group)
admin.site.register(Organization)
admin.site.register(Account, AccountAdmin)