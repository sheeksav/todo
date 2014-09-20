from django import forms


class AddTaskForm(forms.Form):
    description = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'type':'text',
            'placeholder':'Enter task here...',
            'class':'form-control',
        }
    ))

