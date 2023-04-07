from .forms import FirstForm, SecondForm
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
import pickle
import pandas as pd
import sklearn
import ast


# Create your views here.
def firstForm(request):
    if request.method == 'POST':
        form = FirstForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            request.session['first_form'] = form.cleaned_data
            return redirect('second_form')
    else:
        form = FirstForm()
    return render(request, 'form.html', {'form': form})


def secondForm(request):
    if request.method == 'POST':
        form = SecondForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # Do something with form data
            form_data = {**request.session.get('first_form', {}),
                         **form.cleaned_data}  # Combine form data from both forms
            del request.session['first_form']  # Remove first form data from session
            # Do something with combined form data
            return HttpResponseRedirect(reverse('getResult', kwargs={'form_data': form_data}))
    else:
        form_data = request.session.get('first_form', {})  # Get form data from session
        form = SecondForm(initial=form_data)  # Pre-populate form with form data
    return render(request, 'form.html', {'form': form})


def getResult(request, **kwargs):
    form_data = ast.literal_eval(kwargs['form_data'])
    # print(request)
    # print(form_data)
    with open('model_pkl', 'rb') as files:
        loadedModel = pickle.load(files)

    df = pd.DataFrame(columns=['age', 'sex', 'graduated_h_school_type', 'additional_work', 'activity', 'partner',
                               'accomodation', 'reading_non_scientific', 'reading_scientific',
                               'impact_of_projects', 'attendances_classes', 'taking_notes', 'grade_previous',
                               'grade_expected'])
    # personal data
    age = form_data['q1']
    print("here", age)
    sex = form_data['q2']
    graduated_h_school_type = form_data['q3']
    additional_work = form_data['q4']
    activity = form_data['q5']
    partner = form_data['q6']
    accomodation = form_data['q7']

    # academic data
    reading_non_scientific = form_data['q8']
    reading_scientific = form_data['q9']
    impact_of_projects = form_data['q10']
    attendances_classes = form_data['q11']
    taking_notes = form_data['q12']
    grade_previous = form_data['q13']
    grade_expected = form_data['q14']

    df = df.append({
        'age': age,
        'sex': sex,
        'graduated_h_school_type': graduated_h_school_type,
        'additional_work': additional_work,
        'activity': activity,
        'partner': partner,
        'accomodation': accomodation,
        'reading_non_scientific': reading_non_scientific,
        'reading_scientific': reading_scientific,
        'impact_of_projects': impact_of_projects,
        'attendances_classes': attendances_classes,
        'taking_notes': taking_notes,
        'grade_previous': grade_previous,
        'grade_expected': grade_expected
    }, ignore_index=True)

    prediction = loadedModel.predict(df)
    print(prediction)

    return render(request, 'success.html', {'prediction': prediction})
