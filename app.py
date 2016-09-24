import httplib2


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


@app.route('/search', methods = ['GET','POST'])
def search():
    handle = request.form['handle']
    since = request.form['since']
    until = request.form['until']
    return_list = [handle, since, until]
    print(handle, since, until)

    return render_template('tweets.html', api_data = return_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0')