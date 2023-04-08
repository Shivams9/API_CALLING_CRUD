from django.core import serializers
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import crudModel


def create(request):
    try:
        user_name = request.GET["user_name"]
        user_address = request.GET["user_address"]
        user_mobilenumber = request.GET["user_mobilenumber"]
        print("user_mobilenumber", user_mobilenumber)

        # opt = request.GET["option"]
        p = crudModel()
        p.user_name = user_name
        p.user_address = user_address
        p.user_mobilenumber = user_mobilenumber

        p.save()
        print("saved")
        output = [p]
        output = serializers.serialize("json", output)
        result = {"status": "ok", "data": output}
        return JsonResponse(result)
        # return HttpResponse(output, content_type="application/json")
    except:
        error = {"status": "failed"}
        return JsonResponse(error)


# return render(request, "create.html",
#               {"user_name": user_name, "user_address": user_address, "user_mobilenumber": user_mobilenumber,
#                "submit": submit})


def jsonall(request):
    output = serializers.serialize("json", crudModel.objects.all())
    # return JsonResponse(output,safe=False)
    return HttpResponse(output, content_type="application/json")


def read(request):
    crud = crudModel.objects.all()
    output = serializers.serialize("json", crudModel.objects.all())

    return HttpResponse(output, content_type="application/json")
    # return render(request, "read.html", {'cruds': crud})


def edit(request):
    id = request.GET["id"]
    try:
        crud = crudModel.objects.get(id=id)
        crud.user_name='Updated';
        crud.user_address='Updata@12';
        crud.user_mobilenumber='12456789';
        crud.save()
        print(crud)
        crud = [crud]
    except:
        error = {"status": "failed"}
        return HttpResponse("No data")
    output = serializers.serialize("json", crud)
    return HttpResponse(output, content_type="application/json")
    # return render(request, 'edit.html', {'cruds': crud})


def update(request):
    id = request.GET["id"]
    crud = crudModel.objects.get(id=id)
    try:
        if request.POST:
            user_name = request.POST["user_name"]
            # user_address = request.POST["user_address"]
            user_mobilenumber = request.POST["user_mobilenumber"]
            crud.user_name = user_name
            # crud.user_address = user_address
            crud.user_mobilenumber = user_mobilenumber
            crud.save()
            print(crud)
            crud = [crud]
    except:
        error = {"status": "failed"}
        return HttpResponse("data upgrade")
    output = serializers.serialize("json", crud)
    return HttpResponse(output, content_type="application/json")

    # return render(request, 'edit.html', {'cruds': crud})


# delete data in the database
def delete(request):
    try:
        if request.GET:
            id = request.GET["id"]
            crud = crudModel.objects.filter(id=id)[0]
            crud.delete()
            print(crud)
            crud = [crud]
            output = serializers.serialize("json", crud)
            return HttpResponse(output, content_type="application/json")
        return HttpResponse("no id")

    except:
        error = {"status": "failed"}
        return HttpResponse("no data")

    # return render(request, "delete.html", {"cruds": crud})
#
