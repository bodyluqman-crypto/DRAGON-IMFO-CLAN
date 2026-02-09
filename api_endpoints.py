"""
Real Free Fire API Endpoints
"""

# REAL FREE FIRE API ENDPOINTS
FF_API_ENDPOINTS = {
    # Player Endpoints
    "GET_PLAYER_INFO": "https://clientbp.common.ggbluefox.com/GetPlayerPersonalShow",
    "GET_PLAYER_STATUS": "https://clientbp.common.ggbluefox.com/GetPlayerStatus",
    "UPDATE_PLAYER_INFO": "https://clientbp.common.ggbluefox.com/UpdateSocialBasicInfo",
    
    # Clan Endpoints
    "GET_CLAN_INFO": "https://clientbp.common.ggbluefox.com/GetClanInfo",
    "GET_CLAN_MEMBERS": "https://clientbp.common.ggbluefox.com/GetClanMembers",
    "SEARCH_CLAN": "https://clientbp.common.ggbluefox.com/SearchClan",
    
    # Friend Endpoints
    "GET_FRIEND_LIST": "https://clientbp.common.ggbluefox.com/GetFriendList",
    "REMOVE_FRIEND": "https://clientbp.common.ggbluefox.com/RemoveFriend",
    "ADD_FRIEND": "https://clientbp.common.ggbluefox.com/AddFriend",
    
    # Squad Endpoints
    "GET_SQUAD_INFO": "https://clientbp.common.ggbluefox.com/GetSquadInfo",
    "JOIN_SQUAD": "https://clientbp.common.ggbluefox.com/JoinSquad",
    "CREATE_SQUAD": "https://clientbp.common.ggbluefox.com/CreateSquad",
    
    # Authentication Endpoints
    "MAJOR_LOGIN": "https://loginbp.common.ggbluefox.com/MajorLogin",
    "GET_LOGIN_DATA": "https://clientbp.common.ggbluefox.com/GetLoginData",
    
    # Garena Endpoints
    "GARENA_OAUTH": "https://100067.connect.garena.com/oauth/guest/token/grant",
    "GARENA_VERIFY": "https://prod-api.reward.ff.garena.com/redemption/api/auth/inspect_token/",
    
    # Shop Endpoints
    "SHOP2GAME_LOGIN": "https://shop2game.com/api/auth/player_id_login"
}

# REAL HEADERS TEMPLATE
REAL_HEADERS_TEMPLATE = {
    'X-Unity-Version': '2018.4.11f1',
    'ReleaseVersion': 'OB52',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-GA': 'v1 1',
    'Authorization': 'Bearer {token}',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
    'Accept-Encoding': 'gzip'
}

def get_real_headers(token):
    """Get headers with real token"""
    headers = REAL_HEADERS_TEMPLATE.copy()
    headers['Authorization'] = f'Bearer {token}'
    return headers

def create_real_packet(data_type, data):
    """Create real packet structure"""
    packets = {
        "player_info": {
            "1": {"data": data.get("uid")},
            "2": {"data": 1}
        },
        "clan_info": {
            "1": {"data": data.get("clan_id")},
            "2": {"data": 1}
        },
        "clan_members": {
            "1": {"data": data.get("clan_id")},
            "2": {"data": data.get("page", 1)},
            "3": {"data": data.get("limit", 50)}
        }
    }
    
    return packets.get(data_type, {})