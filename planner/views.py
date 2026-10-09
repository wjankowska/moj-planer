from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import PlannerItem
from .forms import PlannerItemForm

@login_required
def dashboard(request):
    items = PlannerItem.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = PlannerItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('dashboard')
    else:
        form = PlannerItemForm()

    # Przygotowanie danych wydarzeń dla biblioteki FullCalendar
    events_data = []
    for item in items:
        # Dobór koloru kafelka w zależności od typu wpisu
        if item.item_type == 'event':
            color = '#10b981'  # zielony (Spotkanie)
        elif item.item_type == 'deadline':
            color = '#f43f5e'  # czerwony (Ważny termin)
        else:
            color = '#3b82f6'  # niebieski (Zadanie)

        events_data.append({
            'title': item.title,
            'start': item.due_date.isoformat(),
            'backgroundColor': color,
            'borderColor': color,
            'textColor': '#ffffff',
            'completed': item.is_completed,
        })

    return render(request, 'planner/dashboard.html', {
        'items': items,
        'form': form,
        'events_json': events_data,
    })

@login_required
def toggle_task(request, item_id):
    item = get_object_or_404(PlannerItem, id=item_id, user=request.user)
    item.is_completed = not item.is_completed
    item.save()
    return redirect('dashboard')

@login_required
def delete_task(request, item_id):
    item = get_object_or_404(PlannerItem, id=item_id, user=request.user)
    item.delete()
    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatyczne logowanie po utworzeniu konta
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})