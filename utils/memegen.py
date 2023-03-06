import requests
import json 

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Key": "fc59484b9bmsh9e243ddc5a3037ep1cc60ajsn4df3798ccd71",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

def memegen():
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    return {'setup':data['body'][0]['setup'], 'punchline':data['body'][0]['punchline'], 'type':data['body'][0]['type'] }
