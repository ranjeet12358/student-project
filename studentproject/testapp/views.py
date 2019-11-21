from django.shortcuts import render
from testapp import forms

# Create your views here.
def student_view(request):
    form=forms.studentregistration()
    if request.method=='POST':
        form=forms.studentregistration(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('data is add in the database sucessfully')
    return render(request,'testapp/demo.html',{'form':form})
