from django import forms
from .models import PlannerItem

class PlannerItemForm(forms.ModelForm):
    class Meta:
        model = PlannerItem
        fields = ['title', 'item_type', 'due_date', 'description']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }