from django.shortcuts import render
from .models import Architect
from .forms import ArchitectForm

# Create your views here.
def home(request):
    return render(request, 'home_page/index.html')

def architects_list(request):
    all_architects = Architect.objects.all
    return render(request, 'architects_db/architects_list.html', {'all':all_architects} )


def add_architect(request):
    if request.method == 'POST':
        form = ArchitectForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'architects_db/add_architect.html',{})

    else:
        return render(request, 'architects_db/add_architect.html',{})