from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse


AUTHORS_INFO = {
    'poe': {
        'id': 1,
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/7/75/Edgar_Allan_Poe_2_retouched_and_transparent_bg.png'
    },
    'borges': {
        'id': 2,
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Jorge_Luis_Borges_1951%2C_by_Grete_Stern.jpg'
    }
}


def authors(request):
    return render(request, 'authors.html', {
        'authors': AUTHORS_INFO
    })


def authors_filtered(request):
    authors = {}
    for author_slug, author in AUTHORS_INFO.items():
        if 'q' in request.GET:
            query = request.GET['q']
            if query not in author['full_name'].lower():
                continue
        authors[author_slug] = author

    return render(request, 'authors.html', {
        'authors': authors
    })


def author_detail_name(request, name):
    if name not in AUTHORS_INFO:
        return HttpResponseNotFound()
    return render(request, 'author_detail.html', {
        'author': AUTHORS_INFO[name]
    })


def author_detail_id(request, author_id):
    author = None
    for author in AUTHORS_INFO.values():
        if author['id'] == author_id:
            author = author
            break
    if not author:
        return HttpResponseNotFound()

    return render(request, 'author_detail.html', {
        'author': author
    })


def author_display(request, name, display):
    if name not in AUTHORS_INFO:
        return HttpResponseNotFound()
    if display == 'list':
        template = 'author_detail.html'
    elif display == 'table':
        template = 'author_detail_table.html'

    return render(request, template, {
        'author': AUTHORS_INFO[name]
    })

def request_info(request):
    # https://docs.djangoproject.com/en/2.0/ref/request-response/
    return render(request, 'request_info.html')


def old_author_page(request, name):
    # return redirect(reverse('author_detail', args=[name]))
    # return redirect(reverse('author_detail', kwargs={'name': name}))

    return redirect('/author/{}/'.format(name))
