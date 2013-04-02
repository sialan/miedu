from django import forms
from campaigns.models import Campaign

class CampaignCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    account = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Campaign
        exclude = ('backers', 'active', 'completed', 'completed', 'consummated', 'currently_featured', 'feature_score', 'caption', 'number_backers', 'amount_pledged', 'completion_date', 'state',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        blueprint = super(CampaignCreationForm, self).save(commit=False)
        if commit:
            also save city country to this user
            blueprint.save()
        return blueprint


class CampaignChangeForm(forms.ModelForm):

    class Meta:
        model = Campaign