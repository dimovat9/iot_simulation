import slack
from datetime import datetime
import os

token_id = os.environ.get('slack_token')
channel_id = os.environ.get('slack_channel')

def sendMessage(title,message):
    client = slack.WebClient(token=token_id)
    client.chat_postMessage(channel=channel_id, text='*' + title + '*', attachments=[{"pretext": "High temperature detected", "text": message}])
