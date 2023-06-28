import requests
import pyttsx3

engine = pyttsx3.init()

ville = "île-de-france"
api_key = "***clée API***"

try:
    reponse = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric')
              #envoie une requête et retourne un objet de réponse
    status_code = reponse.status_code

    if status_code == 200:
        donnees = reponse.json()
        temperature = donnees["main"]["temp"]
        ressenti = donnees["main"]["feels_like"]
        description = donnees["weather"][0]["description"]
                                        
        humidite = donnees["main"]["humidity"]

        print(f"{ville}\n- Température: {temperature}°C \n- Ressentie: {ressenti} \n- Humidité: {humidite}% \n- Déscription: {description}")
        engine.say(f"En {ville} la température est de {temperature} degrés celsus. {description}")
        engine.runAndWait()
    else:
        print("Erreur lors de la récupération des données")


except Exception as e:
    print("Une erreur s'est produite:", e)
