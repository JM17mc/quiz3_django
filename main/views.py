from django.shortcuts import render

def student_list(request):
    student = [
        {"name": "John Michael Mamac", "course": "BSIT", "grade": "3", "email": "jmc123@gmail.com"},
        
        {"name": "Peter Parker", "course": "BSIT", "grade": "2", "email": "pitpark@gmail.com"},
        
        {"name": "Mary Jane", "course": "BSIT", "grade": "1.25", "email": "mjane@gmail.com"},
        
        {"name": "Ned Mac", "course": "BSIT", "grade": "1.5", "email": "nedmac@gmail.com"},
        
    ]

    return render(request, "main/home.html", {"student": student})