from django import forms

class FormName(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget = forms.Textarea)
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)


	def clean_botcatcher(self):
		botcatcher = self.cleaned_data['botcatcher']
		if(botcatcher):
			raise forms.ValidationError("Gotcha Bot!")
		return botcatcher