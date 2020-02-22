from django.views.generic import ListView
from pictures.models import Picture


class PicturesIndexView(ListView):
    template_name = 'pictures/list.html'
    context_object_name = 'pictures'
    # paginate_by = 10
    # paginate_orphans = 1
    model = Picture
    ordering = ['name']

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

