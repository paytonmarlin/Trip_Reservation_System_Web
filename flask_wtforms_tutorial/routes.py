from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *

from .reservations import *
#joe was herer

#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit(): #do error checking
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()

    return render_template("admin.html", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    err = None
    form = ReservationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Get the form data to query the api
            firstName = request.form['first_name']
            lastName = request.form['last_name']
            row = request.form['row']#this is the row
            seat = request.form['seat']#this is the column
        
            ReservationsTest(firstName, row, seat)
#Return the chart here the things above will be passed to the Generat Chart or maybe another method
    GenerateChart() # This writes to chart.txt the current reservations

    chart = imageChart() #This reads the text file and splits line by line


    return render_template("reservations.html", form=form, template="form-template", err = err, chart=chart) #add the chart = chart and error = error

