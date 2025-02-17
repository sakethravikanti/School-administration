from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Data
# Create your views here.
def home(request):
    student=Data.objects.all()
    return render(request,'home.html',{'student':student})
def student_list(request):
    # Query all student records
    students = Data.objects.all()
    # Render the list template with the student data
    return render(request, 'student_list.html', {'student': students})

def student_add(request):
    if request.method == 'POST':
 # Extract data from the form
        name = request.POST.get('name')
        grade = request.POST.get('grade')
        section = request.POST.get('section')
        marks = request.POST.get('marks')
 # Create a new student
        Data.objects.create(
        name=name,
        grade=grade,
        section=section,
        marks=marks,
        )
 # Redirect to the student list after saving
        return redirect('student-list')
 # If GET request, render the form
    return render(request, 'student_form.html')
def student_edit(request, pk):
 # Fetch the student by primary key (ID)
    student = get_object_or_404(Data, pk=pk)
    if request.method == 'POST':
 # Update the student details
        student.name = request.POST.get('name')
        student.grade = request.POST.get('grade')
        student.section = request.POST.get('section')
        student.marks = request.POST.get('marks')
        student.save() # Save changes to the database
        return redirect('student-list')
 # Render the form with existing data
    return render(request, 'student_form.html', {'student': student})

def student_delete(request, pk):
 # Fetch the student by primary key (ID)
    student = get_object_or_404(Data, pk=pk)
    if request.method == 'POST':
        student.delete() # Delete the student record
        return redirect('student-list')
 # Render the delete confirmation page
    return render(request, 'student_confirm_delete.html', {'student': student})