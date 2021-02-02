from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from ratings.models import Rating


def main_view(request):
    obj=Rating.objects.all().order_by("?").first()
    context={
    "object":obj
    }
    return render(request,"ratings/main.html",context)
def rate_image(request):
    if request.method=="POST":
        el_id=request.POST.get('el_id')
        val=request.POST.get('val')
        obj=Rating.objects.get(id=el_id)
        obj.score=val
        obj.save()
        return JsonResponse({'success':'true','score':val},safe=False)
    return JsonResponse({'success':'false'})
