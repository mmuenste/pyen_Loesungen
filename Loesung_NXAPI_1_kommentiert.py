"""
Loesung zum Uebungsblatt zum Thema Nexus-API
"""
import json
import requests
from credentials import username, password, ip
# Import des Moduls 'json' zum Umgang mit dem JSON-Dateiformat,
# Import von 'requests' zum Erstellen des HTTP-POST und Import
# von 'credentials' zum Bereitstellen der Zugangsdaten.

URL = "http://{}/ins".format(ip)  # Einsetzen der IP-Adresse
CRED = (username, password)

# Als Python Dictionary formatierte Abfrage des Nexus-REST-API
COMMAND = {"ins_api": {"version": "1.0",
                       "type": "cli_show",
                       "chunk": "0",
                       "sid": "1",
                       "input": "sho vers",
                       "output_format": "json"
                       }}

# Angabe des Datenaustauschformates, in diesem Fall JSON
HDR = {'Content-type': 'application/json',
       'Accept': 'application/json'}

# Hier erfolgt der eigentliche HTTP-POST aufruf, welcher an die REST API
# uebermittelt wird. Die Funktion 'json.dumps()' wandelt das Python Dictionary
# fuer die Abfrage in das JSON-Format um.
RESP = requests.post(URL, headers=HDR, auth=CRED, data=json.dumps(COMMAND))

RESP_PAYLOAD = RESP.text  # Die Antwort als Text

# Die Funktion json() macht die im JSON-Format erhaltende Antwort als Python
# Dictionary verfuegbar:
BODY = RESP.json()

# Oeffnen einer JSON-Datei zum Schreiben der Rueckgabe
with open('resp.json', 'w') as jsonfile:
    jsonfile.write(RESP.text)
# Abfrage der Processor ID
PRC_BRD_ID = BODY['ins_api']['outputs']['output']['body']['proc_board_id']
print(PRC_BRD_ID)
