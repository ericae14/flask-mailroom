import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation
from model import Donor 

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/create/', methods=['GET', 'POST'])
def create_donation():
    try:
        if request.method == 'POST':
            donor = Donor.select().where(Donor.name == request.form['name']).get()
            # donor = Donor()
            # donor.name = request.form['name']
            donation = Donation(value=request.form['amount'], donor=donor)
            donation.save()
            return redirect(url_for('all'))
    except Exception:
        message = f"{request.form['name']}, is not a valid donor.</br>Please enter a valid donor."
        return render_template('create.jinja2', error=message)

    return render_template('create.jinja2')
    



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

