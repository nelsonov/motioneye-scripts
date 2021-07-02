#!/usr/bin/python3

from slack_sdk import WebClient
import os
import sys

slack_token = os.environ["SLACK_API_TOKEN"]
sc = WebClient(slack_token)
alert=sys.argv[1]

sc.chat_postMessage(
    channel='homeassistant',
    text=alert
)
