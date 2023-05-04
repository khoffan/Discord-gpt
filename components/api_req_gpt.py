import requests

def API_showchatgpt(event):
    url = "https://openai80.p.rapidapi.com/chat/completions"
    usr_msg = event
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": usr_msg
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "ae41b5ea99msh1ecd12bfa2aefeap16b035jsn3d6134450248",
        "X-RapidAPI-Host": "openai80.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_jason = response.json()
        msg = response_jason["choices"][0]["message"]["content"]
        return msg
    else:
        return response.text

# user_in = input("Enter msg: ")
# print(f"bot send: "+str(API_showchatgpt(user_in)))

