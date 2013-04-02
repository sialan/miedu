from django import forms
from campaigns.models import Campaign

class CampaignCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    class Meta:
        model = Campaign

    def save(self, commit=True):
        # Save the provided password in hashed format
        blueprint = super(CampaignCreationForm, self).save(commit=False)
        if commit:
            blueprint.save()
        return user


class CampaignChangeForm(forms.ModelForm):

    class Meta:
        model = Campaign