from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.

def home(request):
    chai_variety = ChaiVariety.objects.all()
    return render(request, 'chai/index.html',{'chai_variety':chai_variety})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai':chai})

def chai_store(request):
    stores=None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(
                chai_varieties=chai_variety
            )
    else:
        form = ChaiVarietyForm()
    return render(request, 'chai/chai_store.html',{'stores':stores, 'form':form})