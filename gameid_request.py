import authenticated_requests

yahoo_session = authenticated_requests.oauth_session()
mlb_request = "https://fantasysports.yahooapis.com/fantasy/v2/game/mlb"

response = authenticated_requests.make_auth_query(yahoo_session, mlb_request)
print(response['fantasy_content']['game'])