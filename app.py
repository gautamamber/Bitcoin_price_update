from flask import Flask, render_template
import requests
app = Flask("__name__")
@app.route('/')
def home():
	r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
	v = r.json()['bpi']['USD']['rate']
	return render_template('index.html', v=v)

if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug = True)  
