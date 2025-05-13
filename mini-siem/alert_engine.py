import requests

def send_slack_alert(ip, count):
    webhook_url = "https://hooks.slack.com/services/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"

    message = {
        "text": f"🚨 ALERT: {ip} has triggered {count} failed SSH login attempts!"
    }

    response = requests.post(webhook_url, json=message)

    if response.status_code != 200:
        print(f"Failed to send Slack alert: {response.status_code}, {response.text}")
