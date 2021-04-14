from django import forms
# from todo.models import Priority


# PRIORITY_CHOISE = ((i.id, i.name) for i in Priority.objects.all())


class ToDoForm(forms.Form):
    name = forms.CharField(max_length=60)
    # priority = forms.ChoiceField(choices=PRIORITY_CHOISE)
