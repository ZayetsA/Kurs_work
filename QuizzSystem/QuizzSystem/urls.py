from django.contrib import admin
from django.urls import path
from quizApplicationWords import views as a
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', a.main),
                  path('welcome/', a.welcome),
                  path('quiz/', a.index),
                  path('save_ans/', a.save_ans, name="saveans"),
                  path('result/', a.result, name="result"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
