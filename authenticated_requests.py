from yahoo_oauth import OAuth2
import xmltodict


def oauth_session():
    # Authenticate using oauth credentials
    # New users: Create 'oauth2.json' yourself and copy the format in oauth2Sample.json
    oauth = OAuth2(None, None, from_file='oauth2.json')
    if not oauth.token_is_valid():
        oauth.refresh_access_token()
    return oauth


def make_auth_query(yahoo_sesh, query):
    # Pass all queries through here
    response = yahoo_sesh.session.get(query)
    if response.status_code != 200:
        print("Got a bad status on request: {}", response.status_code)
    else:
        return xmltodict.parse(response.content)
