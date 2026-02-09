"""
Real Free Fire Authentication Module
"""
import requests
import json
import time

class FreeFireAuth:
    """Authentication with real Free Fire API"""
    
    def __init__(self):
        self.real_jwt = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjo5MjgwODkyMDE4LCJuaWNrbmFtZSI6IkJZVEV2R3QwIiwibm90aV9yZWdpb24iOiJNRSIsImxvY2tfcmVnaW9uIjoiTUUiLCJleHRlcm5hbF9pZCI6ImYzNGQyMjg0ZWJkYmFkNTkzNWJjOGI1NTZjMjY0ZmMwIiwiZXh0ZXJuYWxfdHlwZSI6NCwicGxhdF9pZCI6MCwiY2xpZW50X3ZlcnNpb24iOiIxLjEwNS41IiwiZW11bGF0b3Jfc2NvcmUiOjAsImlzX2VtdWxhdG9yIjpmYWxzZSwiY291bnRyeV9jb2RlIjoiRUciLCJleHRlcm5hbF91aWQiOjMyMzQ1NDE1OTEsInJlZ19hdmF0YXIiOjEwMjAwMDAwNSwic291cmNlIjoyLCJsb2NrX3JlZ2lvbl90aW1lIjoxNzE0NjYyMzcyLCJjbGllbnRfdHlwZSI6MSwic2lnbmF0dXJlX21kNSI6IiIsInVzaW5nX3ZlcnNpb24iOjEsInJlbGVhc2VfY2hhbm5lbCI6ImlvcyIsInJlbGVhc2VfdmVyc2lvbiI6Ik9CNDUiLCJleHAiOjE3MjIwNTkxMjF9.yYQZX0GeBMeBtMLhyCjSV0Q3e0jAqhnMZd3XOs6Ldk4"
        
    def get_headers(self):
        """Get real Free Fire headers"""
        return {
            'X-Unity-Version': '2018.4.11f1',
            'ReleaseVersion': 'OB52',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-GA': 'v1 1',
            'Authorization': f'Bearer {self.real_jwt}',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
            'Accept-Encoding': 'gzip'
        }
    
    def get_player_info_real(self, uid):
        """Get real player info from Free Fire"""
        url = "https://clientbp.common.ggbluefox.com/GetPlayerPersonalShow"
        headers = self.get_headers()
        
        # Create proper packet structure
        data = {
            "1": uid,
            "2": 1
        }
        
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(data),
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
        except:
            pass
        
        return None
    
    def get_clan_info_real(self, clan_id):
        """Get real clan info from Free Fire"""
        url = "https://clientbp.common.ggbluefox.com/GetClanInfo"
        headers = self.get_headers()
        
        data = {
            "clan_id": clan_id
        }
        
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(data),
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
        except:
            pass
        
        return None

# Export auth instance
ff_auth = FreeFireAuth()