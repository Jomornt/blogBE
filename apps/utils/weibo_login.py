
def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_uri = "http://127.0.0.1:8000/complete/weibo"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={redirect_uri}".format(client_id=2744546942, redirect_uri=redirect_uri)
    print(auth_url)

def get_access_token(code="3cadf937b5739e6363848f71853cedfd"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url, data={
        "client_id": "2744546942",
        "client_secret": "ef956adfb5943c86de459f0969822bbf",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://127.0.0.1:8000/complete/weibo",
    })
    pass

def get_user_info(access_token="", uid=""):
    user_url = "https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}".format(token=access_token, uid=uid)
    print(user_url)

if __name__ == "__main__":
    # get_auth_url()
    # get_access_token(code="3cadf937b5739e6363848f71853cedfd")
    get_user_info(access_token="2.00jpxHCHKCqjzC0ae1272563L1P2NB", uid="6444380795")