from flask import Flask, render_template, json, request, redirect, jsonify

import tweepy
import json

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


#Prints tweets for one handle
@app.route('/search', methods = ['GET','POST'])
def search():

    handles = ["KingJames", "KyrieIrving", "kevinlove", "TheRealJRSmith", "Channing_Frye", "imanshumpert", "RealTristan13", "mowilliams"]
    names = ["LeBron James", "Kyrie Irving", "Kevin Love", "J.R. Smith", "Channing Frye", "Iman Shumpert", "Tristan Thompson", "Mo Williams"]
    dictionary = dict(zip(names, handles))

    name = request.form['name']
    handle = dictionary[name]


    since = "2015-09-21"
    count = 0

    return_dict = {}
    tweets = []
    for result in tweepy.Cursor(api.search, q="from:"+handle, since=since).items():
        count = count + 1
        tweets.append(result.text)

    with open('stats.json') as stats_data:
        stats = json.load(stats_data)

    player_run = stats[name][0]/4377
    player_ballhold = stats[name][1]/5.23
    player_pass = (stats[name][2]/stats[name][3])/1.2
    player_turnover = stats[name][4]/0.2
    player_touch = stats[name][5]/80
    player = {"run": player_run, "ballhold": player_ballhold, "pass": player_pass, "turnover": player_turnover, "touch": player_touch}

    with open('stats_cavs.json') as stats_data:
        stats_cavs = json.load(stats_data)

    avg_run = stats_cavs["avg_run"]
    avg_ballhold = stats_cavs["avg_ballhold"]
    avg_pass = stats_cavs["avg_pass"]
    avg_turnover = stats_cavs["avg_turnover"]
    avg_touch = stats_cavs["avg_touch"]

    average = {"run": avg_run, "ballhold": avg_ballhold, "pass": avg_pass, "turnover": avg_turnover, "touch": avg_touch}

    return_dict = {"handle": handle, "count": count, "player": player, "average": average, "tweets": tweets}
    json_return_dict = json.dumps(return_dict)

    print return_dict
    # list_return_dict = [return_dict]
    return render_template('tweets.html', api_data = [json_return_dict, return_dict])
    # return json(api_data)


@app.route('/calculate_team_average')
def calculate():
    with open('stats.json') as stats_data:
        stats = json.load(stats_data)

    total_run = 0
    total_ballhold = 0
    total_pass_made = 0
    total_pass_received = 0
    total_turnover = 0
    total_touch = 0
    handles = ["KingJames", "KyrieIrving", "kevinlove", "TheRealJRSmith", "Channing_Frye", "imanshumpert", "RealTristan13", "mowilliams"]
    names = ["LeBron James", "Kyrie Irving", "Kevin Love", "J.R. Smith", "Channing Frye", "Iman Shumpert", "Tristan Thompson", "Mo Williams"]
    for i in range(0, len(handles)):
        stats_player = stats[names[i]] 
        print stats_player

        DIST_RUN_OFF_METERS = stats_player[0]
        AVG_SEC_PER_TCH = stats_player[1]
        PASSES_MADE = stats_player[2]
        PASSES_RECEIVED = stats_player[3]
        DRIVE_TOV_PCT = stats_player[4]
        NUM_TOUCHES = stats_player[5]

        total_run = total_run + DIST_RUN_OFF_METERS
        total_ballhold = total_ballhold + AVG_SEC_PER_TCH
        total_pass_made = total_pass_made + PASSES_MADE
        total_pass_received = total_pass_received + PASSES_RECEIVED
        total_turnover = total_turnover + DRIVE_TOV_PCT
        total_touch = total_touch + NUM_TOUCHES

    avg_run = (total_run/4377)/len(handles)
    avg_ballhold = (total_ballhold/5.23)/len(handles)
    avg_pass = ((total_pass_made/total_pass_received)/1.2)

    avg_turnover = (total_turnover/0.2)/len(handles)
    avg_touch = (total_touch/80)/len(handles)

    json_output = {"avg_run": avg_run, "avg_ballhold": avg_ballhold, "avg_pass": avg_pass, "avg_turnover": avg_turnover, "avg_touch": avg_touch}
    with open("stats_cavs.json","wb") as f:
        f.write(json.dumps(json_output))

    return render_template('index.html')


#Creates JSON for all handles in list 
@app.route('/search_all', methods = ['GET','POST'])
def search_all():
    #2014-2015 source: http://www.usatoday.com/story/sports/nba/2014/10/27/nba-teams-announced-their-opening-day-rosters-for-the-2014-15-season/18035777/
    # handles = ["StephenCurry30", "Money23Green", "hbarnes", "KlayThompson", "festus", "TheBlurBarbosa", "JustHolla7", "andre", "ShaunLivingston", "Dlee042", "Mospeights16", "BRush_25"]
    # handles = []
    # handles = ["DeMar_DeRozan", "Klow7", "Cory_Joe", "JValanciunas", "T_DotFlight31", "npowell2404", "pdpatt", "jtthekid", "pskills43", "Bebe92", "Bruno_Caboclo", "EJSingler", "delonwright", "bradyheslip"]
    # handles = ["gallinari8888", "JaValeMcGee34", "KennethFaried35", "emmanuelmudiay", "wilsonchandler", "nurkic23", "MikeMiller_13", "thats_G_", "WillTheThrillB5", "DarrellArthur00", "jameernelson", "bigplaydj1", "Mbeasy5", "NateWolters", "JarnellStokes",]
    # handles = ["KDTrey35", "russwest44", "RealStevenAdams", "VicOladipo", "Enes_Kanter", "Dsabonis11", "FlyDre21", "alexabrines", "campayne", "1JOLOLO", "KyleSingler", "nickcollison4", "MrAnthonyMorrow", "jhuestis", "NazrMohammed", "DakariJohnson"]
    # handles = ["antic12pero", "24Bazemore", "DeMarreCarroll1", "Al_Horford", "JohnnyCashVU23", "ShelvinMack", "Paulmillsap4", "mikemuscala", "Adreian_Payne", "DennisMike93", "mikescott", "ThaboSefolosha", "Teague0", "KyleKorver", "TheRealEB42"]
    # handles = ["bestbetbass", "unclejeffgreen", "KellyOlynyk", "philpressey", "RajonRondo", "smart_MS3", "Jared _Sully0", "OfficialMT23", "thekidet", "realjamesyoung", "ZellerTyler", "DwightPowell33"]

    playerlist = []
    for handle in handles:
        since = "2015-09-21" #arbitrary date way in the past
        count = 0

        return_dict = {}
        tweets = []
        for result in tweepy.Cursor(api.search, q="from:"+handle, since=since).items():
            count = count + 1
            tweets.append(result.text)

        return_dict = {"handle": handle, "count": count, "tweets": tweets}
        playerlist.append(return_dict)

    json_output = {"players": playerlist}

    with open("cavs.json","wb") as f:
        f.write(json.dumps(json_output))

    return render_template('tweets_all.html', api_data = json_output)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
