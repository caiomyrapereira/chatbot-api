from ..models import StartChat

def init():
    import json
    from ibm_watson import AssistantV2
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

    import warnings
    warnings.filterwarnings('ignore')

    apikey = 'lVINcGCE1S8a-jkSu_CNQSoiLMEY34wUVexas1BkPedz'
    url = 'https://api.au-syd.assistant.watson.cloud.ibm.com/instances/394180ae-4b81-46a8-9254-0385c5bd81e2'
    assistantID = '4687a278-1100-4348-a3f8-e90dc9e2168e'

    authenticator = IAMAuthenticator(apikey)
    assistant = AssistantV2(
        version='2018-09-20',
        authenticator=authenticator)
    assistant.set_service_url(url)
    assistant.set_disable_ssl_verification(True)

    session = assistant.create_session(assistantID).get_result()
    session_json = json.dumps(session, indent=2)
    session_dict = json.loads(session_json)
    session_id = session_dict['session_id']
    print(session_id)

    print('******* INICIANDO CONVERSA')
    message = assistant.message(
        assistantID,
        session_id, ).get_result()
    message_json = json.dumps(message, indent=2)
    message_dict = json.loads(message_json)
    for i in range(len(message_dict['output']['generic'])):
        valor = message_dict['output']['generic'][i]['text']
    papo = StartChat()
    papo.chat = valor
    return papo
