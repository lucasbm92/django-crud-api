import os
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

# Django settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    SECRET_KEY="your-secret-key",
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
    ],
)

# View
def hello_world(request):
    return HttpResponse("Hello world")

# URL patterns
urlpatterns = [
    path("", hello_world),
]

if __name__ == "__main__":
    execute_from_command_line()