from django.shortcuts import render


# Create your views here.

def main_view(request):
    if request.method == "GET":
        name = request.GET.get('name', None)
        message = request.GET.get('message', None)

        context = {
            'name': name,
            'message': message
        }

        return render(request, 'main.html', context=context)
