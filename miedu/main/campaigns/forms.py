from django import forms
from taggit.forms import *
from campaigns.models import Campaign

class CampaignCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    def __init__(self, *args, **kwargs):
        self.fields['account'] = args[0].user

    account = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))    
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'placeholder':'Ottawa, Toronto, or Montreal...'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'placeholder':'Canada, Ireland, or USA...'}))
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder':'When will your fundin'}))
    minimum_pledge = forms.IntegerField(label='Minimum Pledge', widget=forms.TextInput(attrs={'placeholder':'5, 20, or more...'}))
    goal = forms.IntegerField(label='Funding Goal', widget=forms.TextInput(attrs={'placeholder':'5000, 10000, or more...'}))

    
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder':'Something short for yourself...'}))
    headline = forms.CharField(label='Main Heading', widget=forms.TextInput(attrs={'placeholder':'Something catchy for supporters...'}))
    # description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    call_to_action = forms.CharField(label='Call to Action', widget=forms.TextInput(attrs={'placeholder':'Get people interested...'}))
    tags = TagField(widget=forms.TextInput(attrs={'placeholder':'tech, html5, social'}))
    #summary = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


    #inlineformsetcampaignmilestone
    #inlineformsetcampaignfaqitem


    class Meta:
        model = Campaign
        exclude = ('backers', 'active', 'completed', 'completed', 'consummated', 'currently_featured', 'feature_score', 'caption', 'number_backers', 'amount_pledged', 'completion_date', 'state', 'endline', 'multimedia', 'start_date',)

    def save(self, commit=True):
        # convert dates to datetime
        blueprint = super(CampaignCreationForm, self).save(commit=False)
        if commit:
            # also save city country to this user
            blueprint.save()
        return blueprint


class CampaignChangeForm(forms.ModelForm):

    class Meta:
        model = Campaign