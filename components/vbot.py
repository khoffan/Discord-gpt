from components.api_req_gpt import API_showchatgpt
from components.th2eng import th_2_eng

def show_message(user_in):
    try:
        trans_eng = th_2_eng(user_in)
        responces = API_showchatgpt(trans_eng)
        return responces
        # if(detect_leng == "en"):
        #     responces = API_showchatgpt(trans_eng)
        #     print(f"\n {responces} \n")
        # else:
        #     responces = API_showchatgpt(trans_eng)
        #     print(f"\n {responces} \n")
    except Exception as e:
        return e
        

# while True:
#     user_input = input("Enter message: ")
#     if user_input == "end" or user_input == "bye":
#         break
#     print(f"BOt send: {show_message(user_input)}")
