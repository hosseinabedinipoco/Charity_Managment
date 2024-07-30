from django.shortcuts import render
from django.http import HttpResponse
from account.models import User
# Create your views here.
def about_us(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, 'about_us.html', {'users':users})
    else:
        return 'mehod not allowed'  