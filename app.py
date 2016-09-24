# from twitter import *
# import twitter
#
#
# api = twitter.Api(consumer_key='xHE1qE7M4OXMDs5sMEcGjDOFF',
#                   consumer_secret='AYZz4eudZQOzPPlN1rcxOoK5tzobkLEMnpmRXflr99DJlFaAPY',
#                   access_token_key='119321740-pSopqVovkWTD7VbCh34YJ72HVJbxWasGcAru7t1m',
#                   access_token_secret='Fhs4YYFOHYQxY4AH5wmzEdeRJDTlBvIeM2okdG4IdsB6Y')


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


@app.route('/twitter')
def twitter():

    for result in tweepy.Cursor(api.search, q="to:KingJames", since="2016-09-20", until="2016-09-22").items():
        print result.text
        if result:
            print result.text
        else:
            print ('no data')

    # for result in api.search("nba"):
    #     print result.text
    #     if result:
    #         print result.text
    #     else:
    #         print ('no data23')

    return render_template('twitter.html')
    # return json(api_data)




if __name__ == "__main__":
    app.run(host='0.0.0.0')
