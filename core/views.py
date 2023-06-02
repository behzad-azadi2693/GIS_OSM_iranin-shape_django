from django.shortcuts import render
import pandas as pd
from .models import Roads
from django.conf import settings
import os

# read the Excel file into a Pandas DataFrame
# Create your views here.
def index(request):
    


    return render(render, 'index.html')