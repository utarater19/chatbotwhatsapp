import os
import dialogflow_v2 as dialogflow

# Set Google Application Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ipibotwa-pjpp-64760ae21520.json"

# Initialize Dialogflow session client
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "ipibotwa-pjpp"

def detect_intent_from_text(text, session_id, language_code='en'):
    """
    Detect intent from text using Dialogflow API.

    Args:
        text (str): User input text.
        session_id (str): Unique session identifier.
        language_code (str): Language code for the query (default: 'en').

    Returns:
        dialogflow.types.QueryResult: Query result from Dialogflow.
    """
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(query, session_id):
    """
    Fetch the reply from Dialogflow based on user query.

    Args:
        query (str): User input query.
        session_id (str): Unique session identifier.

    Returns:
        str: Fulfillment text response from Dialogflow.
    """
    response = detect_intent_from_text(query, session_id)
    return response.fulfillment_text
