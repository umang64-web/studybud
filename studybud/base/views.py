from django.shortcuts import redirect, render
from django.http import HttpResponse
# from base.form import Employee
from base.form import StudentForm
from base.functions.functions import handle_uploaded_file

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Design with me!'},
    {'id':3, 'name':'Frontend developers'},
]


# def index(request):
#     if request.method == 'POST':
#         student = StudentForm(request.POST, request.FILES)
#         if student.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponse("File Uploaded Successfuly")
#     else:
#         student = StudentForm()
#         return render(request, "index.html", {'form':student})





# def index(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 return redirect('/')
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request, 'index.html', {'form' : form})



def index(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form' : form})
    

def methodinfo(request):
    return HttpResponse("Http request is " + request.method)


def getdata(request):
    data = StudentForm.objects.get(id = 12)
    return HttpResponse(data)

def home(request):
    return render(request,'home.html')


def room(request, roomno):
    context  = {'roomno':roomno}
    return render(request,'room.html',context)

def main(request):
    return render(request,'main.html')

