from django import forms


class ToDoForm(forms.Form):
    name = forms.CharField(max_length=60)
    priority = forms.ChoiceField(
        choices=()
    )

    def __init__(self, *args, **kwargs):
        priority_choices = kwargs.pop('priority_choices', ())
        super().__init__(*args, **kwargs)
        self.fields['priority'].choices = priority_choices
