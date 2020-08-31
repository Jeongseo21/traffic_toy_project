from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    import xmltodict
    import requests
    # 사용자가 업무 데이터를 입력했을 시 = POST
    if request.method =="POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            #업무 List 데이터
            all_items = List.objects.all
            messages.success(request, ('업무를 추가했습니다.'))
            # api 돌발 상황 데이터
            api_request1 = requests.get("http://openapi.seoul.go.kr:8088/password/xml/AccInfo/1/5/")
            api = xmltodict.parse(api_request1.content)
            data = api['AccInfo']['row']
            #api_request가 가져왔으면 데이터를 xml_dict로 파싱해서 저장

            return render(request, 'home.html', { 'data':data, 'all_items':all_items })
    else:
        # 업무 List 데이터
        all_items = List.objects.all

        # api 돌발 상황 데이터
        api_request1 = requests.get("http://openapi.seoul.go.kr:8088/password/xml/AccInfo/1/5/")
        api = xmltodict.parse(api_request1.content)
        data = api['AccInfo']['row']

        return render(request, 'home.html', { 'data':data, 'all_items':all_items })


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,'삭제되었습니다.')
    return redirect('home')

def cross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

