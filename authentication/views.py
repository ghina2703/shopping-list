from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # Check if 'username' and 'password' keys are present in request.POST
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is not None and password is not None:
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    # Status login sukses.
                    return JsonResponse({'status': 'success'})
                else:
                    return JsonResponse({'status': 'inactive'})
            else:
                return JsonResponse({'status': 'invalid_credentials'})
        else:
            return JsonResponse({'status': 'missing_fields'})
    else:
        # Handle cases where the request method is not POST
        return JsonResponse({'status': 'method_not_allowed'})

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)