from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, 'index.html', {"":""})


def result(request):
    if request.method == 'POST':
        if request.POST['result'] != "":
            result = request.POST['result']
            print(result)

            return TemplateResponse(request, 'index.html', {'post_result': result})
        else:
            return TemplateResponse(request, 'index.html', {"":""})
    else:
        return TemplateResponse(request, 'index.html', {"": ""})

