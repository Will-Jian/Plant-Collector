from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Fertilizer
from .forms import WateringForm

'''plants = [
  {'species': 'Hibiscus', 'hardinessZones': '5-11', 'nativeArea': 'Asia, North America'},
  {'species': 'Jasmine', 'hardinessZones': '6-10', 'nativeArea': 'Eurasia, Africa, Australasia, Oceania'}
]
'''
# Create your views here.
# Define the home view
def assoc_fertilizer(request, plant_id, fertilizer_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Plant.objects.get(id=plant_id).fertilizers.add(fertilizer_id)
  return redirect('detail', plant_id=plant_id)


def unassoc_fertilizer(request, plant_id, fertilizer_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Plant.objects.get(id=plant_id).fertilizers.remove(fertilizer_id)
  return redirect('detail', plant_id=plant_id)



def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request,'about.html')


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html',{ 'plants': plants})

def plants_detail(request,plant_id):
    plant = Plant.objects.get(id=plant_id)
    id_list = plant.fertilizers.all().values_list('id')
    fertilizers_plant_doesnt_have = Fertilizer.objects.exclude(id__in=id_list)
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {'plant':plant, 'watering_form':watering_form, 'fertilizers':fertilizers_plant_doesnt_have})

def add_watering(request, plant_id):
 # create a ModelForm instance using the data in request.POST
  form = WateringForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_watering = form.save(commit=False)
    new_watering.plant_id = plant_id
    new_watering.save()
    return redirect('detail', plant_id=plant_id)


class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
success_url = '/plants/{plant_id}'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['hardiness','description']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'

class FertilizerList(ListView):
  model = Fertilizer

class FertilizerDetail(DetailView):
  model = Fertilizer

class FertilizerCreate(CreateView):
  model = Fertilizer
  fields = '__all__'

class FertilizerUpdate(UpdateView):
  model = Fertilizer
  fields = ['name', 'type']

class FertilizerDelete(DeleteView):
  model = Fertilizer
  success_url = '/fertilizers'