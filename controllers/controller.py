from flask import render_template, request, redirect
from app import app
from models.events_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events/new')
def show_task_form():
    return render_template ('new_event.html')

@app.route('/events', methods=['POST'])
def add_new():
    event_title = request.form['title']
    event_description = request.form['description']
    event_date = request.form['date']
    event_num_guests = request.form['num_guests']
    event_location = request.form['location']
    new_event = Event(event_title, event_description,event_date,event_num_guests,event_location)
    add_new_event(new_event)
    return redirect('/events')




