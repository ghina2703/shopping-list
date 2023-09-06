from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Ghina Nabila Gunawan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
    
# from django.shortcuts import render berguna untuk mengimpor fungsi render 
# dari modul django.shortcuts. Fungsi render digunakan untuk me-render tampilan HTML 
# dengan menggunakan data yang diberikan.


