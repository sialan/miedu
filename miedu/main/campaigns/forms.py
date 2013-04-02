from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from campaigns.models import Campaign

class CampaignCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    
    class Meta:
        model = Campaign
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


class CampaignChangeForm(forms.ModelForm):

    class Meta:
        model = Campaign