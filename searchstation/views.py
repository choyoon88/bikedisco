from django.shortcuts import render


# Create your views here.
def get_searchstation(request):
    return render(request, 'searchstation_folder/searchstation.html')
