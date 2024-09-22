#
# Copyright (C) 2024 @TISnoob
#
# SPDX-License-Identifier: Apache-2.0
#


import requests
import os

# Configuration
FACEBOOK_PAGE_ID = "YOUR_FACEBOOK_PAGE_ID"
ACCESS_TOKEN = os.environ["FACEBOOK_ACCESS_TOKEN"]
DISCORD_WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

def fetch_latest_post():
    url = f"https://graph.facebook.com/v12.0/{FACEBOOK_PAGE_ID}/posts?access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    
    if 'data' in data and len(data['data']) > 0:
        return data['data'][0]  # Get the latest post
    return None

def send_to_discord(content):
    json_payload = {
        "embeds": [{
            "title": "New Facebook Post!",
            "description": content.get('message', 'No content available'),
            "url": f"https://www.facebook.com/{FACEBOOK_PAGE_ID}/posts/{content['id'].split('_')[1]}",
            "color": 7506394,
            "footer": {
                "text": "Posted from Facebook"
            }
        }]
    }
    
    requests.post(DISCORD_WEBHOOK_URL, json=json_payload)

def main():
    latest_post = fetch_latest_post()
    
    if latest_post:
        send_to_discord(latest_post)

if __name__ == "__main__":
    main()
