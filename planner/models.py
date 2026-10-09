from django.db import models
from django.contrib.auth.models import User

class PlannerItem(models.Model):
    ITEM_TYPES = [
        ('event', 'Wydarzenie / Spotkanie'),
        ('task', 'Zadanie do wykonania'),
        ('deadline', 'Ważna data / Termin'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planner_items')
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(blank=True, verbose_name="Opis")
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES, default='task')
    due_date = models.DateTimeField(verbose_name="Termin / Data")
    is_completed = models.BooleanField(default=False, verbose_name="Wykonane")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f"[{self.get_item_type_display()}] {self.title}"
