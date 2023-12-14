from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from ap1.models import Reteta


class RetetaView(ListView):
    model = Reteta
    template_name = 'ap1/reteta_index.html'
    paginate_by = 5

class IstoricView(ListView):
    model = Reteta
    template_name = 'ap1/istoric_index.html'
    paginate_by = 10


class CreateRetetaView(LoginRequiredMixin,CreateView):
    model = Reteta
    fields = ['nume', 'text_reteta', 'timp_executie']
    template_name = 'forms.html'
    def get_success_url(self):
        return reverse('ap1:lista_retete')


class UpdateRetetaView(LoginRequiredMixin,UpdateView):
    model = Reteta
    fields = ['nume', 'text_reteta', 'timp_executie']
    template_name = 'forms.html'
    def get_success_url(self):
        return reverse('ap1:lista_retete')


@login_required
def deactivate_reteta(request, pk):
    Reteta.objects.filter(id=pk).update(active=0)
    return redirect('ap1:lista_retete')


@login_required
def activate_reteta(request, pk):
    Reteta.objects.filter(id=pk).update(active=1)
    return redirect('ap1:lista_retete')


@login_required
def delete_reteta(request, pk):
    Reteta.objects.filter(id=pk).delete()
    return redirect('ap1:lista_retete')