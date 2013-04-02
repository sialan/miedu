from django import forms
from campaigns.models import Campaign

class CampaignCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    __init__ set account,city,country

    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder':'Title of the blueprint...'}))
    account = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'placeholder':'Current city...'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'placeholder':'Current country...'}))


    minimum_pledge = forms.IntegerField(label='Minimum Pledge', widget=forms.NumberInput(attrs={'placeholder':'Minimum amount of support...'}))
    goal = forms.IntegerField(label='Funding Goal', widget=forms.NumberInput(attrs={'placeholder':'Total funding goal...'}))



    headline = forms.CharField(label='Main Heading', widget=forms.TextInput(attrs={'placeholder':'Main heading...'}))

    
    call_to_action = forms.CharField(label='Call to Action', widget=forms.TextInput(attrs={'placeholder':'Draw in support...'}))


    class Meta:
        model = Campaign
        exclude = ('backers', 'active', 'completed', 'completed', 'consummated', 'currently_featured', 'feature_score', 'caption', 'number_backers', 'amount_pledged', 'completion_date', 'state', 'endline',)

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