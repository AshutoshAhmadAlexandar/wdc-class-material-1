from django.urls import path

from . import views


urlpatterns = [
    # Step 4
    path('authors/', views.authors, name='authors'),

    # Step 5
    path('authors_filtered/', views.authors_filtered, name='authors_filtered'),

    # Step 6
    path('author/<slug:name>/', views.author_detail_name, name='author_detail'),

    # Step 7
    path('author-by-id/<int:author_id>/', views.author_detail_id, name='author_by_id'),

    # Step 8
    path('author-as-list/<slug:name>/', views.author_display, {'display': 'list'}, name='author_as_list'),

    # Step 9
    path('author-as-table/<slug:name>/', views.author_display, {'display': 'table'}, name='author_as_table'),

    # Step 10
    path('request-info/', views.request_info, name='request_info'),

    # Step 10
    path('old-author-page/<slug:name>/', views.old_author_page, name='old_author_page'),
]
