from django.shortcuts import redirect

def api_root_view(request):
    """
    Redirects to the API root URL.
    """
    return redirect('api-root')