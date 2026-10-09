from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PlannerItem
from .forms import PlannerItemForm

@login_required
def dashboard(request):
    # Pobieramy wpisy należące TYLKO do zalogowanego użytkownika
    items = PlannerItem.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = PlannerItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user  # Przypisujemy zadanie do Twojego konta
            item.save()
            return redirect('dashboard')
    else:
        form = PlannerItemForm()

    return render(request, 'planner/dashboard.html', {'items': items, 'form': form})

@login_required
def toggle_task(request, item_id):
    # Bezpieczne odznaczanie / oznaczanie jako wykonane
    item = get_object_or_404(PlannerItem, id=item_id, user=request.user)
    item.is_completed = not item.is_completed
    item.save()
    return redirect('dashboard')
