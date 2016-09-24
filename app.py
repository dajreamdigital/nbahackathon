from flask import Flask, render_template, json, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    return render_template('index.html', api_data="")


@app.route('/twitter')
def twitter():
    return render_template('twitter.html', api_data="")



if __name__ == "__main__":
    app.run(host='0.0.0.0')
