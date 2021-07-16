from flask import Flask, flash, render_template, request, redirect, session
from forex_python.converter import CurrencyRates, CurrencyCodes
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey666"

@app.route("/")
def show_form():
	"""Display homepage with form"""

	return render_template("home.html")

T = CurrencyRates()
curr = CurrencyCodes()


@app.route("/conversion", methods = ['GET', 'POST'])
def conversion():
	"""Converting the amount from c1 currency to c2 currency"""
	
	if request.method == 'POST':
		c1 = request.form.get('convert-from', None)
		c2 = request.form.get('convert-to', None)
		amt = request.form.get('amount', None)

		if not amt.isdigit():	
			flash('Please enter a valid number')
			return redirect("/")
		else:	
			rate = T.convert(c1, c2, int(amt))
			symbol = curr.get_symbol(c2)

			details = {'c1': c1, 'c2': c2, 'amt': amt, 'symbol': symbol, 'rate': rate}

	return render_template("result.html", details=details)



@app.route("/home-btn", methods = ["GET"])
def return_to_homepage():
	"""Return to homepage"""

	return redirect("/")

