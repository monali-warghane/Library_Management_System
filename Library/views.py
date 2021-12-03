from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView, FormView
from .models import AddBooks, IssueBook, Returnbook
from django.views.generic.edit import FormView
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

class addbooks(CreateView):
    model = AddBooks
    fields = '__all__'
    template_name = 'addbooks.html'
    success_url = '/'

class viewbooks(TemplateView):
    template_name = 'viewbooks.html'

    def get_context_data(self, **kwargs):
        context = super(viewbooks, self).get_context_data(**kwargs)
        context["viewbooks"] = AddBooks.objects.all()
        return context


class issuebook(CreateView):
    model = IssueBook
    fields = '__all__'
    template_name = 'issuebook.html'
    # form_class = IssueBook
    success_url = '/issuedbook'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

class returnbook(CreateView):
    model = Returnbook
    fields = '__all__'
    template_name = 'returnbook.html'
    success_url = '/returnbook'

class issuedbook(TemplateView):
    template_name = 'issuedbook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issuebook'] = IssueBook.objects.all()
        return context

class updatebook(UpdateView):
    model = AddBooks
    fields = '__all__'
    template_name = 'update.html'
    success_url = '/'

def registeradmin(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
    context = {'form': form}
    return render(request,'admin.html', context)

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')


    context = {}
    return render(request, 'login.html', context)



class deletebook(DeleteView):
    template_name = 'delete.html'
    model = AddBooks
    success_url = '/'



