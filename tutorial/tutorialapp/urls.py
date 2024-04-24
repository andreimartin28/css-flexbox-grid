from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from tutorialapp import views

urlpatterns = [

     path("",
          views.index,
          name="index"),

     path('flex/',
          views.flex,
          name='flex'),

     path('grid/',
          views.grid,
          name='grid'),

     path('gridd/',
          views.gridd,
          name='gridd'),

     path('grid_3/',
          views.grid_3,
          name='grid_3'),

     path('grid_4/',
          views.grid_4,
          name='grid_4'),

     path('grid_5/',
          views.grid_5,
          name='grid_5'),

     path('article-layout/',
          views.article_layout,
          name='article-layout'),

     path('grid-flexbox/',
          views.grid_flexbox,
          name='grid-flexbox')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
