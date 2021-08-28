import math

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .forms import PersonForm
from .forms import Triangle
from .models import Person
from .models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ...   # same as above, no changes needed.


def triangle(request):
    gip = None
    if request.method == 'POST':
        form = Triangle(request.POST)
        if form.is_valid():
            kat1 = form.cleaned_data['kat1']
            kat2 = form.cleaned_data['kat2']
            gip = round(math.sqrt(kat1 ** 2 + kat2 ** 2), 2)
    else:
        form = Triangle()

    return render(request,
                  'polls/triangle.html',
                  {'gip': gip,
                   'form': form})


def person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Спасибо, новый пользователь создан!')
    data = {'form': form}
    return render(request, 'polls/person.html', context=data)


def person_id(request, p_id):
    obj = get_object_or_404(Person, pk=p_id)
    form = PersonForm(instance=obj)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные сохранены')
    data = {'form': form}
    return render(request, 'polls/person.html', context=data)
