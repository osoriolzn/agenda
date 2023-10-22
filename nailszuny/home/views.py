from django.shortcuts import render
import calendar
import datetime

def index(request):
    context = {
        'title': 'Nails Zuny'
    }
    return render(request, 'index.html', context)

def agenda(request):
    def current_month(month):
        months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        month -= 1
        return months[month]

    year = 2023
    month = 10
    create_calendar = calendar.monthcalendar(year, month)
    month_letter = current_month(month)

    date = datetime.datetime.now()
    current_day = date.day

    context = {
        'title': 'Agenda',
        'year': year,
        'month': month,
        'month_letter': month_letter,
        'current_day': current_day,
        'calendar': create_calendar
    }
    return render(request, 'agenda.html', context)
