from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contacto
from .forms import ContactoForm

# Vistas de Contactos protegidas
class ContactoListView(LoginRequiredMixin, ListView):
    model = Contacto
    template_name = 'contactos/contacto_list.html'
    context_object_name = 'contactos'
    paginate_by = 10

class ContactoCreateView(LoginRequiredMixin, CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contactos/contacto_form.html'
    success_url = reverse_lazy('contacto_list')

class ContactoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contactos/contacto_form.html'
    success_url = reverse_lazy('contacto_list')

class ContactoDeleteView(LoginRequiredMixin, DeleteView):
    model = Contacto
    template_name = 'contactos/contacto_confirm_delete.html'
    success_url = reverse_lazy('contacto_list')

# Creación de nuevos usuarios
class RegistroUsuarioView(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('contacto_list')