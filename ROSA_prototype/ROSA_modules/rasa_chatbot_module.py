import requests
import json
import uuid

def conversation_id_verifier(username, last_username, guid):
    if ((username!=last_username) and (username!="")):
        guid = conversation_id_generator()
    return guid


def conversation_id_generator():
    guid = str(uuid.uuid4())
    return guid


def api_chat(fala, guid):

    #Primeira Chamada:
    # http://localhost:5005/conversations/{conversation_id}/messages

    pload = {'text':fala,'sender':'user'}

    headers = {
        'Content-Type': "application/json",
    }
    r = requests.request("POST",'http://localhost:5005/conversations/'+guid+'/messages', data = json.dumps(pload), headers=headers)
    r_dictionary = r.json()
    intent = r_dictionary['latest_message']['intent']['name']

    # Segunda Chamada:
    # http://localhost:5005/conversations/{conversation_id}/trigger_intent
    pload = {'name':intent}
    r = requests.request("POST",'http://localhost:5005/conversations/'+guid+'/trigger_intent', data = json.dumps(pload), headers=headers)
    r_dictionary = r.json()
    if r_dictionary['messages'] != []:
        response = r_dictionary['messages'][0]['text']
    else:
        response = ""

    return intent, response