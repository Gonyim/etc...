import random
import json
import requests

# 액세스 토큰 로드 함수
def load_access_token():
    with open("access_token.txt", "r") as file:
        access_token = file.read().strip()
    return access_token

KAKAO_TOKEN = load_access_token()

# 카카오톡 나에게 보내기 설정
def send_to_kakao(text):
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
    }

    data = {"template_object": json.dumps(post)}
    try:
        response = requests.post(url, headers=header, data=data)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("카카오톡 전송 중 오류 발생:", e)
        return None

count = 0
lotto_numbers = []

while count < 6:
    new_number = random.randint(1, 45)
    if new_number not in lotto_numbers:
        lotto_numbers.append(new_number)
        count += 1

lotto_numbers.sort()
text = ' '.join(map(str, lotto_numbers))  # 리스트를 문자열로 변환
r = send_to_kakao(text)

if r is not None:
    print(r)
