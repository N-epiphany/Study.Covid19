from django.shortcuts import render
from .stateanalysisfunction import stateanalysis
from .districtanalysisfunction import districtanalysis


def home(request):
    return render(request, 'home.html')

def world(request):
    return render(request, 'world.html')

def india(request):
    return render(request, 'india.html')

def contact(request):
    return render(request, 'contact.html')

# Create your views here.
def state_analysis_view(request):
    if request.method == 'POST':
        state_name = request.POST.get('state_name')
        result = stateanalysis(state_name)

        context = {
            'result': result
        }
        return render(request, 'state.html', context)

    return render(request, 'state.html')

def district_analysis_view(request):
    if request.method == 'POST':
        district_name = request.POST.get('district_name')
        result = districtanalysis(district_name)

        context = {
            'result': result
        }
        return render(request, 'district.html', context)

    return render(request, 'district.html')


