from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.core.serializers import serialize

import json
from django.views.decorators.csrf import csrf_exempt
from .models import Record
from .forms import RecordForm
from django.shortcuts import get_object_or_404, redirect

@csrf_exempt
def index(request):
    if request.method == "POST":
        if 'HTTP_USER_AGENT' in request.META and 'Postman' in request.META['HTTP_USER_AGENT']:
            try:
                data = json.loads(request.body.decode('utf-8'))  
            except json.JSONDecodeError as e:
                return JsonResponse({'error':'Invalid JSON data:{}'.formate(str(e))},status=400)
            form = RecordForm(data)

        if form.is_valid():
            form.save()
            if 'HTTP_USER_AGENT' in request.META and 'Postman' in request.META['HTTP_USER_AGENT']:
                return JsonResponse({'message': 'Data saved Successfully'}, status=201)

        else:
            if 'HTTP_USER_AGENT' in request.META and 'Postman' in request.META['HTTP_USER_AGENT']:
                return JsonResponse({'errors': form.errors}, status=400)
            

@csrf_exempt
def update(request, id):
    record = get_object_or_404(Record, id = id)

    if request.method == "POST":
        if 'HTTP_USER_AGENT' in request.META and 'Postman' in request.META['HTTP_USER_AGENT']:
            try:
                data = json.loads(request.body.decode('utf-8'))  
            except json.JSONDecodeError as e:
                return JsonResponse({'error':'Invalid JSON data:{}'.formate(str(e))},status=400)
            form = RecordForm(data, instance=record)

        if form.is_valid():
            form.save()
            if 'HTTP_USER_AGENT' in request.META and 'Postman' in request.META['HTTP_USER_AGENT']:
                return JsonResponse({'message': 'Data updated Successfully'}, status=201)

        else:
            if 'HTTP_USER_AGENT' in request.META and 'Postman' in request.META['HTTP_USER_AGENT']:
                return JsonResponse({'errors': form.errors}, status=400)
            
@csrf_exempt
def delete(request, id):
    record = get_object_or_404(Record, id = id)
    if 'HTTP_USER_AGENT' in request.META and 'Postman' in request.META['HTTP_USER_AGENT']:
        record.delete()
        return JsonResponse({'message': 'Data deleted Successfully'}, status=200)
    
    elif request.method == "DELETE":
        record.delete()
        return JsonResponse({'message': 'Data deleted Successfully'}, status=200)
    
    else:
        return JsonResponse({'errors': 'Method not allowed'}, status=405)
    

def select(request):
    record = Record.objects.all()
    if 'HTTP_USER_AGENT' in request.META and 'Postman' in request.META['HTTP_USER_AGENT']:
        serialized_data = serialize('json', record)
        return JsonResponse(serialized_data, safe=False)

    




