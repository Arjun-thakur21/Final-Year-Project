# filepath: /d:/Arjun/project/bearing-fault-diagnosis/bearing_fault_diagnosis/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .data_analysis import analyze_and_train
import pandas as pd
import logging
import os
from django.conf import settings
from diagnosis.models import Contact

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')

def savecontact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        en=Contact(name=name, email=email, message=message)
        en.save()
    return render(request, 'index.html')

def diagnose(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('inputFile')

        if uploaded_file:
            file_extension = uploaded_file.name.split('.')[-1].lower()
            logger.info(f"Uploaded file extension: {file_extension}")

            try:
                if file_extension == 'xlsx':
                    df = pd.read_excel(uploaded_file, engine='openpyxl')
                elif file_extension == 'xls':
                    df = pd.read_excel(uploaded_file, engine='xlrd')
                else:
                    logger.error("Invalid file format")
                    return HttpResponse("Invalid file format")
            except Exception as e:
                logger.error(f"Error reading the file: {e}")
                return HttpResponse(f"Error reading the file: {e}")

            analysis_results = analyze_and_train(df)

            # Paths to the saved plots
            plot_save_path = settings.PLOT_SAVE_PATH
            rmse_plot = os.path.join(plot_save_path, 'rmse.png')

            return render(request, 'diagnosis_result.html', {
                'results': analysis_results,
                'rmse_plot': rmse_plot
            })

    return HttpResponse("Invalid request")