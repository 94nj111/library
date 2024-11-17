from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpRequest

from catalog.models import Book, Author, LiteraryFormat


def index(request):
    context = {
        "num_books": Book.objects.count(),
        "num_authors": Author.objects.count(),
        "num_literary_formats": LiteraryFormat.objects.count(),
    }
    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    
    
def test_session_view(request: HttpRequest) -> HttpResponse:
    request.session["book"] = "Test session book"
    return HttpResponse(
        "<h1>Test Session</h1>"
    )
