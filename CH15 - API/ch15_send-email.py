
import requests

def send_simple_message():
    return requests.post(
    "https://api.mailgun.net/v3/sandbox4fdfa14e84ca499597756a69741b5c88.mailgun.org/messages",
        auth=("api", "input_api_code"),
        data={"from": "Excited User <mailgun@sandbox4fdfa14e84ca499597756a69741b5c88.mailgun.org>",
              "to": ["kirsty.2.bradley@bt.com", "leannehagger@gmail.com", "kirsty.2.bradley@bt@sandbox4fdfa14e84ca499597756a69741b5c88.mailgun.org"],
              "subject": "Hello, let's see what is going to happen",
              "text": "Let's hope this works, Mailgun awesomness!"})

send_simple_message()

