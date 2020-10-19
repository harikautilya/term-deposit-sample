from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import datetime
import joblib
import json
import pandas as pd
# Create your views here.
def MainView(request):
    now = datetime.datetime.now()
    return render(request, "form.html") 

@csrf_exempt
def ApiView(request):

    default_label = {'no': 0, 'yes': 1}
    job_label = {'admin.': 0, 'blue-collar': 1, 'entrepreneur': 2, 'housemaid': 3, 'management': 4, 'retired': 5, 'self-employed': 6, 'services': 7, 'student': 8, 'technician': 9, 'unemployed': 10, 'unknown': 11}
    marital_label = {'divorced': 0, 'married': 1, 'single': 2}
    education_label = {'primary': 0, 'secondary': 1, 'tertiary': 2, 'unknown': 3}
    housing_label = {'no': 0, 'yes': 1}
    loan_label = {'no': 0, 'yes': 1}
    contact_label = {'cellular': 0, 'telephone': 1, 'unknown': 2}
    poutcome_label = {'failure': 0, 'other': 1, 'success': 2, 'unknown': 3}
    
    now = datetime.datetime.now()
   
    age = request.POST.get("age",-1)
    campaign = request.POST.get("campaign",-1) 
    pdays = request.POST.get("pdays",-1)
    
    default = request.POST.get("default","")
    job = request.POST.get("job","")
    marital = request.POST.get("marital",-1)

    education = request.POST.get("education",-1)
    balance = request.POST.get("balance",-1)
    housing = request.POST.get("housing",-1)

    loan = request.POST.get("loan",-1)
    contact = request.POST.get("contact",-1)
    duration = request.POST.get("duration",-1)

    poutcome = request.POST.get("poutcome",-1)

    model_input = [default_label.get(default), job_label.get(job), marital_label.get(marital), education_label.get(education), housing_label.get(housing), loan_label.get(loan), contact_label.get(contact), poutcome_label.get(poutcome), int(age), int(campaign), int(pdays), int(balance)]
    print(model_input)
    loaded_model = joblib.load(settings.BASE_DIR / 'term' /'model.joblib')
    probabilities = loaded_model.predict_proba([model_input])
    predicted = loaded_model.predict([model_input])
    ml_output = pd.DataFrame(probabilities, columns=loaded_model.classes_)
    data_out = json.loads(ml_output.T.to_json())
    no_percentage = data_out["0"]["0"]
    yes_percentage = data_out["0"]["1"]
    html = "<html><body>Yes percentage is now {}.No percentage is now {}.</body></html>".format(yes_percentage, no_percentage)
    return HttpResponse(html)
