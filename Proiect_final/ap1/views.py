from django.views.generic import ListView

from ap1.models import Reteta


class RetetaView(ListView):
    model = Reteta
    template_name = 'ap1/reteta_index.html'