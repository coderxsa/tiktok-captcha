# code is patched does not work you cannot fix or update as the server has changed 
# but gives you a example so dont get scamed if some one is selling 90% will be this layout.

import requests
import base64
import time
import random

from urllib.parse import urlencode
from utils.solver import PuzzleSolver
# credits @ultve
class Solver:
    def __init__(self, did, iid):
        self.__host       = "verification-va.tiktokv.com"
        self.__device_id  = did 
        self.__install_id = iid 
        self.__cookies    = ""
        self.__client     = requests.Session()
# credits @ultve
    def __params(self):
        params = {
            "lang": "en",
            "app_name": "musical_ly",
            "h5_sdk_version": "2.26.17",
            "sdk_version": "1.3.3-rc.7.3-bugfix",
            "iid": self.__install_id,
            "did": self.__device_id,
            "device_id": self.__device_id,
            "ch": "beta",
            "aid": "1233",# credits @ultve
            "os_type": "0",
            "mode": "",
            "tmp": f"{int(time.time())}{random.randint(111, 999)}",
            "platform": "app",
            "webdriver": "false",# credits @ultve
            "verify_host": f"https://{self.__host}/",
            "locale": "en",
            "channel": "beta",
            "app_key": "",
            "vc": "18.2.15",# credits @ultve
            "app_verison": "18.2.15",
            "session_id": "",
            "region": ["va", "US"],
            "use_native_report": "0",
            "use_jsb_request": "1",# credits @ultve
            "orientation": "1",
            "resolution": ["900*1552", "900*1600"],
            "os_version": ["25", "7.1.2"],
            "device_brand": "samsung",
            "device_model": "SM-G973N",# credits @ultve
            "os_name": "Android",
            "challenge_code": "1105",
            "app_version": "18.2.15",
            "subtype": "",# credits @ultve
        }

        return urlencode(params)
# credits @ultve
    def __headers(self) -> dict:

        headers = {# credits @ultve
            "passport-sdk-version": "19",
            "sdk-version": "2",
            "x-ss-req-ticket": f"{int(time.time())}{random.randint(111, 999)}",# credits @ultve
            "cookie": self.__cookies,
            "content-type": "application/json; charset=utf-8",
            "host": self.__host,# credits @ultve
            "connection": "Keep-Alive",
            "user-agent": "okhttp/3.10.0.1",
        }

        return headers
# credits @ultve
    def __get_challenge(self) -> dict:

        params = self.__params()

        req = self.__client.get(
            url = (
                "https://"
                    + self.__host
                    + "/captcha/get?"# credits @ultve
                    + params
            ),
            headers = self.__headers()
        )

        return req.json()

    def __solve_captcha(self, url_1: str, url_2: str) -> dict:
        puzzle = base64.b64encode(
            self.__client.get(# credits @ultve
                url_1,
            ).content
        )
        piece = base64.b64encode(
            self.__client.get(
                url_2,
            ).content# credits @ultve
        )
        
        solver = PuzzleSolver(puzzle, piece)
        maxloc = solver.get_position()# credits @ultve
        randlength = round(
            random.random() * (100 - 50) + 50
        )
        time.sleep(1) # don't remove delay or it will fail
        return {
            "maxloc": maxloc,
            "randlenght": randlength
        }

    def __post_captcha(self, solve: dict) -> dict:
        params = self.__params()

        body = {# credits @ultve
            "modified_img_width": 552,
            "id": solve["id"],
            "mode": "slide",
            "reply": list(# credits @ultve
                {
                    "relative_time": i * solve["randlenght"],
                    "x": round(
                        solve["maxloc"] / (solve["randlenght"] / (i + 1))
                    ),
                    "y": solve["tip"],# credits @ultve
                }
                for i in range(# credits @ultve
                    solve["randlenght"]
                )
            ),
        }

        headers = self.__headers()
# credits @ultve
        req = self.__client.post(
            url = (
                "https://"
                    + self.__host
                    + "/captcha/verify?"# credits @ultve
                    + params
            ),
            headers = headers.update(# credits @ultve
                    {
                        "content-type": "application/json"
                }
            ),
            json = body
        )# credits @ultve

        return req.json()
# credits @ultve
    def solve_captcha(self):
        __captcha_challenge = self.__get_challenge()

        __captcha_id = __captcha_challenge["data"]["id"]# credits @ultve
        __tip_y = __captcha_challenge["data"]["question"]["tip_y"]

        solve = self.__solve_captcha(# credits @ultve
            __captcha_challenge["data"]["question"]["url1"],
            __captcha_challenge["data"]["question"]["url2"],
        )
        
        solve.update(# credits @ultve
                {
                    "id": __captcha_id,
                    "tip": __tip_y# credits @ultve
            }
        )
        # credits @ultve
        return self.__post_captcha(solve)



if __name__ == "__main__":# credits @ultve
    __device_id = ""
    __install_id = ""# credits @ultve
    
    print(
        Solver(
            did = __device_id,
            iid = __install_id# credits @ultve
        ).solve_captcha()
    )
# credits @ultve