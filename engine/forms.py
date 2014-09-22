from django import forms


class AddTaskForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'type':'textarea',
            'placeholder':'Enter title here...',
            'class':'form-control',
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'type':'text',
            'placeholder':'Enter description here...',
            'class':'form-control',
        }
    ))

