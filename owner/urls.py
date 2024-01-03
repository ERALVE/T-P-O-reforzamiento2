from django.urls import path
from . import views

urlpatterns = [
    #path('owner_list/', views.owner_list, name='owner_list'),
    path('owner_orm/', views.owner_orm, name='owner_orm'),
    #path('owner_search/', views.owner_search, name='owner_search'),
    path('owner_details/', views.owner_details, name='owner_details'),

    path('owner_delete/<int:id_owner>', views.owner_delete, name='owner_delete'),
    #path('owner_edit/<int:id_owner>', views.owner_edit, name="owner_edit"),
    path('owner_create/', views.owner_create, name='owner_create'),

    #URL para las vistas basadas en clase
    #path('owner_list_vc/', views.OwnerList.as_view(), name="owner_list_vc"),
    #path('owner_create_vc/', views.OwnerCreate.as_view(), name="owner_create_vc"),
    #path('owner_edit_vc/<int:pk>', views.OwnerUpdate.as_view(), name="owner_edit_vc"),
    #path('owner_delete_vc/<int:pk>', views.OwnerDelete.as_view(), name="owner_delete_vc"),

    #URLs Django Framework drf
    #path('owner_list_drf_def/', views.Owner_api_view, name="owner_list_drf_def"),
    #path('owner_detail_drf_def/<int:pk>', views.owner_details_view, name="owner_detail_drf_def"),

    #Reforzamiento 3
    path('owner_list/', views.owner_list, name='owner_list'),
    path('owner_search/', views.owner_search, name='owner_search'),
    path('owner_delete/', views.owner_delete, name='owner_delete'),
    path('owner_update/<int:id_owner>/', views.owner_update, name='owner_update'),
    path('owner_list_vc/', views.OwnerList.as_view(), name="owner_list_vc"),
    path('owner_create_vc/', views.OwnerCreate.as_view(), name="owner_create_vc"),
    path('owner_update_vc/<int:pk>', views.OwnerUpdate.as_view(), name="owner_update_vc"),
    path('owner_delete_vc/<int:pk>', views.OwnerDelete.as_view(), name="owner_delete_vc"),
    path('owner_post_drf/', views.create_owner, name="owner_post_drf"),
    path('owner_get_drf/', views.list_owners, name="owner_get_drf"),
    path('owner_detail_drf/<int:pk>/', views.owner_details_view, name="owner_detail_drf"),
]