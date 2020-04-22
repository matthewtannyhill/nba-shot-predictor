from __future__ import unicode_literals

from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import fields
from api.models import Campaign
from api.serializers import CampaignSerializer
import json
import stripe

from django.shortcuts import render
from django.http import HttpResponse


class CampaignList(APIView):
    '''Get all campaigns or create a campaign'''
    @csrf_exempt
    def get(self, request, format=None):
        camps = Campaign.objects.all()
        if request.query_params.get('id'):
            camps = camps.filter(title__contains=request.query_params.get('id'))
        serializer = CampaignSerializer(camps, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CampaignDetail(APIView):
    '''Work with an individual Campaign object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        camp = Campaign.objects.get(id=pk)
        serializer = CampaignSerializer(camp)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        camp = Campaign.objects.get(id=pk)
        serializer = CampaignSerializer(camp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        camp = Campaign.objects.get(id=pk)
        camp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Prediction API

def loginView(request):
# this view will pull up the submit html template
        return render(request, "login.html", {})

def nbahomeView(request):
# this view will pull up the submit html template
        return render(request, "nbahome.html", {})

def indexView(request):
# this view will pull up the submit html template
        return render(request, "prediction.html", {})

def resultsView(request):
# this view receives parameters from the submit html template and calls the API in azure
# this contains API code for Python and Python3 

    # If you are using Python 3+, import urllib instead of urllib2
    #import urllib2.request
    import urllib
    import json

    print("_______________________ Request ________________________")
    print()
    print(request)
    print()

    our_data = {
                "Inputs": {
                    "input1": {
                    "ColumnNames": [
                        "TOUCH_TIME",
                        "SHOT_CLOCK",
                        "SHOT_DIST",
                        "CLOSE_DEF_DIST",
                        "FGM",
                        "player_name",
                        "DRIBBLEScr"
                    ],
                    "Values": [
                        [
                        request.POST['TOUCH_TIME'],
                        request.POST['SHOT_CLOCK'],
                        request.POST['SHOT_DIST'],
                        request.POST['CLOSE_DEF_DIST'],
                        0,
                        request.POST['player_name'],
                        request.POST['DRIBBLEScr']
                        ]
                    ]
                    }
                },
                "GlobalParameters": {}
                }

    # First Model
    # the API call
    body = str.encode(json.dumps(our_data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/fcd0755517244a9196f7950ed432dbfb/services/31cdb2c6b8ff45e19b6e0b30f1e6ec2e/execute?api-version=2.0&details=true'
    api_key = '869F6B1laWyXPQwvDkghY7MB7eDleos27ESC0BPNIlWC0t2M4adWQ4+p8fH2WGptOQI+hy//FvVgFBPmam8jMA=='
    # Replace my url and api_key with your own values
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    # If you are using Python 3+, replace urllib2 with urllib.request
    #req = urllib2.Request(url, body, headers)
    req = urllib.request.Request(url, body, headers) 

    # python3 uses urllib while python uses urllib2
    #response = urllib2.request.urlopen(req)
    response = urllib.request.urlopen(req)

    # this formats the results 


    result = response.read()
    result = json.loads(result) # turns bits into json object

    print(result["Results"])
    print(result["Results"]["output1"])
    print(result["Results"]["output1"]["value"])
    print(result["Results"]["output1"]["value"]["Values"])
    print(result["Results"]["output1"]["value"]["Values"][0])
    print(result["Results"]["output1"]["value"]["Values"][0][7])

    result = result["Results"]["output1"]["value"]["Values"][0][7]


    return render(request, "results.html", {"result": result}) # this path assumes that this file is in the root directory in a folder named templates


def coach2indexView(request):
# this view will pull up the submit html template
        return render(request, "coach2prediction.html", {})

def coach2resultsView(request):
# this view receives parameters from the submit html template and calls the API in azure
# this contains API code for Python and Python3 

    # If you are using Python 3+, import urllib instead of urllib2
    #import urllib2.request
    import urllib
    import json

    print("_______________________ Request ________________________")
    print()
    print(request)
    print()

    our_data = {
                "Inputs": {
                    "input1": {
                    "ColumnNames": [
                        "TOUCH_TIME",
                        "SHOT_CLOCK",
                        "SHOT_DIST",
                        "CLOSE_DEF_DIST",
                        "FGM",
                        "player_name",
                        "DRIBBLEScr"
                    ],
                    "Values": [
                        [
                        request.POST['TOUCH_TIME'],
                        request.POST['SHOT_CLOCK'],
                        1,
                        request.POST['CLOSE_DEF_DIST'],
                        request.POST['FGM'],
                        request.POST['player_name'],
                        request.POST['DRIBBLEScr']
                        ]
                    ]
                    }
                },
                "GlobalParameters": {}
                }

    # First Model
    # the API call
    body = str.encode(json.dumps(our_data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/fcd0755517244a9196f7950ed432dbfb/services/0e29d722a67347c980ff96eed79c201a/execute?api-version=2.0&details=true'
    api_key = 'ktVYJDa+fIIxNzDF7qDOqWd8kB18JOFjYXt/K/L/CbB3Rd3vBB2q/tJbLYx9qMbgOWBNym4bh4M85id85vyQxQ=='
    # Replace my url and api_key with your own values
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    # If you are using Python 3+, replace urllib2 with urllib.request
    #req = urllib2.Request(url, body, headers)
    req = urllib.request.Request(url, body, headers) 

    # python3 uses urllib while python uses urllib2
    #response = urllib2.request.urlopen(req)
    response = urllib.request.urlopen(req)

    # this formats the results 


    result = response.read()
    result = json.loads(result) # turns bits into json object

    print(result["Results"])
    print(result["Results"]["output1"])
    print(result["Results"]["output1"]["value"])
    print(result["Results"]["output1"]["value"]["Values"])
    print(result["Results"]["output1"]["value"]["Values"][0])
    print(result["Results"]["output1"]["value"]["Values"][0][7])

    result = result["Results"]["output1"]["value"]["Values"][0][7]


    return render(request, "coach2results.html", {"result": result}) # this path assumes that this file is in the root directory in a folder named templates



def agentindexView(request):
# this view will pull up the submit html template
        return render(request, "agentprediction.html", {})

def agentresultsView(request):
# this view receives parameters from the submit html template and calls the API in azure
# this contains API code for Python and Python3 

    # If you are using Python 3+, import urllib instead of urllib2
    #import urllib2.request
    import urllib
    import json

    print("_______________________ Request ________________________")
    print()
    print(request)
    print()

    our_data = {
                "Inputs": {
                    "input1": {
                    "ColumnNames": [
                        "NBA_DraftNumber",
                        "Salary",
                        "Age",
                        "G",
                        "MP",
                        "OWS",
                        "DWS",
                        "WS"
                    ],
                    "Values": [
                        [
                        request.POST['NBA_DraftNumber'],
                        0,
                        request.POST['Age'],
                        request.POST['G'],
                        request.POST['MP'],
                        request.POST['OWS'],
                        request.POST['DWS'],
                        request.POST['WS']
                        ]
                    ]
                    }
                },
                "GlobalParameters": {}
                }

    # First Model
    # the API call
    body = str.encode(json.dumps(our_data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/63c20b3b0cb64292ab6adbb2bac52a3f/services/e75dc8e551914ca99de048b95e411ec8/execute?api-version=2.0&details=true'
    api_key = 'OzOQ8Ur/7y6dvketa4yylM52KfVKU+TfzYXkqLF0JBeCm15nS3f+Mk/Ivt4kTZLsWirxMK5WxU4VkQqvMUr+Fg=='
    # Replace my url and api_key with your own values
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    # If you are using Python 3+, replace urllib2 with urllib.request
    #req = urllib2.Request(url, body, headers)
    req = urllib.request.Request(url, body, headers) 

    # python3 uses urllib while python uses urllib2
    #response = urllib2.request.urlopen(req)
    response = urllib.request.urlopen(req)

    # this formats the results 


    result = response.read()
    result = json.loads(result) # turns bits into json object

    print(result["Results"])
    print(result["Results"]["output1"])
    print(result["Results"]["output1"]["value"])
    print(result["Results"]["output1"]["value"]["Values"])
    print(result["Results"]["output1"]["value"]["Values"][0])
    print(result["Results"]["output1"]["value"]["Values"][0][8])

    result = result["Results"]["output1"]["value"]["Values"][0][8]

    return render(request, "agentresults.html", {"result": result}) # this path assumes that this file is in the root directory in a folder named templates



def addView(request):
# this view will pull up the submit html template
        return render(request, "add.html", {})

def addresultsView(request):
# this view receives parameters from the submit html template and calls the API in azure
# this contains API code for Python and Python3 

    result = "You have successfully added a new row to the database!"

    # If you are using Python 3+, import urllib instead of urllib2
    #import urllib2.request
    import urllib
    import json

    # Using pyodbc

    # import pyodbc

    # server = 'nbashots.database.windows.net'
    # database = 'nbashotsdb'
    # username = 'group2-4'
    # password = 'Rootbeer24'
    # driver= '{ODBC Driver 17 for SQL Server}'
    # cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    # cursor = cnxn.cursor()

    # cursor.execute("SELECT COUNT(*) FROM dbo.nba_shots_cleaned")  
    # count = list(cursor)
    # print(count)
    # print(count[0][0])
    # index = count[0][0] + 100000
    
    # #sql = "INSERT INTO dbo.nba_shots_cleaned VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # val = (index, request.POST['LOCATION'], request.POST['PERIOD'], request.POST['SHOT_CLOCK'], request.POST['TOUCH_TIME'], request.POST['SHOT_DIST'], request.POST['PTS_TYPE'], request.POST['CLOSEST_DEFENDER'], request.POST['CLOSEST_DEFENDER_PLAYER_ID'], request.POST['CLOSE_DEF_DIST'], request.POST['FGM'], request.POST['player_name'], request.POST['player_id'], request.POST['Player_Team'], request.POST['Defender_Team'], request.POST['Month'], request.POST['GAME_CLOCK_TOTAL_SECONDS'], request.POST['DRIBBLEScr'], request.POST['SHOT_NUMBERln'])
    # cursor.execute(sql, val)
     
    # cnxn.commit()



    # Using pymssql

    # import pymssql
    # import _mssql

    # server = 'nbashots.database.windows.net'
    # database = 'nbashotsdb'
    # user = 'group2-4'
    # password = 'Rootbeer24'
    # port = "1433"
    # cnxn = pymssql.connect(server, port, user, password, database)
    # cursor = cnxn.cursor()

    # cursor.execute("SELECT COUNT(*) FROM dbo.nba_shots_cleaned")  
    # count = list(cursor)
    # print(count)
    # print(count[0][0])
    # index = count[0][0] + 100000
    
    # sql = "INSERT INTO dbo.nba_shots_cleaned VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # val = (index, request.POST['LOCATION'], request.POST['PERIOD'], request.POST['SHOT_CLOCK'], request.POST['TOUCH_TIME'], request.POST['SHOT_DIST'], request.POST['PTS_TYPE'], request.POST['CLOSEST_DEFENDER'], request.POST['CLOSEST_DEFENDER_PLAYER_ID'], request.POST['CLOSE_DEF_DIST'], request.POST['FGM'], request.POST['player_name'], request.POST['player_id'], request.POST['Player_Team'], request.POST['Defender_Team'], request.POST['Month'], request.POST['GAME_CLOCK_TOTAL_SECONDS'], request.POST['DRIBBLEScr'], request.POST['SHOT_NUMBERln'])
    # cursor.execute(sql, val)
     
    # cnxn.commit()



    return render(request, "addresults.html", {"result": result}) # this path assumes that this file is in the root directory in a folder named templates
