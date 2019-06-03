import pandas as pd
from django.shortcuts import render
from titanic import services
# Create your views here.


def titanic_home(request):
    return render(request, 'titanic/titanic_main.html')


def titanic_get_result(request):
    try:
        temp_dict = request.POST.dict()
        output_tray = {1: 'Surviving', 0: 'Not Surviving'}
        data = pd.DataFrame(temp_dict, index=[0])
        prediction, confidence = services.predict(data)

    except Exception as e:
        raise e
    return render(request, 'titanic/titanic_result.html',
                  {'prediction': output_tray[prediction],
                   'prediction_confidence': round(max(confidence[0])*100, 2)})
