from flask import Flask, render_template, json, request, redirect, jsonify

import tweepy

auth = tweepy.OAuthHandler('xHE1qE7M4OXMDs5sMEcGjDOFF', 'AYZz4eudZQOzPPlN1rcxOoK5tzobkLEMnpmRXflr99DJlFaAPY')
auth.set_access_token('119321740-pSopqVovkWTD7VbCh34YJ72HVJbxWasGcAru7t1m', 'Fhs4YYFOHYQxY4AH5wmzEdeRJDTlBvIeM2okdG4IdsB6Y')

api = tweepy.API(auth)


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
    since = "2015-09-21"
    count = 0

    return_dict = {}
    tweets = []
    for result in tweepy.Cursor(api.search, q="from:"+handle, since=since).items():
        count = count + 1
        tweets.append(result.text)
        print result.text
    print (count)

    return_dict = {"handle": handle, "count": count, "tweets": tweets}

    print return_dict
    return render_template('tweets.html', api_data = return_dict)
    # return json(api_data)

@app.route('/search_all', methods = ['GET','POST'])
def search_all():
    handles = []
    playerlist = []
    for handle in handles:
        since = "2015-09-21"
        count = 0

        return_dict = {}
        tweets = []
        for result in tweepy.Cursor(api.search, q="from:"+handle, since=since).items():
            count = count + 1
            tweets.append(result.text)
            print result.text
        print (count)

        return_dict = {"handle": handle, "count": count, "tweets": tweets}
        playerlist.append(return_dict)
    json_output = {"players": playerlist}
    return render_template('tweets.html', api_data = json_output)





if __name__ == "__main__":
    app.run(host='0.0.0.0')
