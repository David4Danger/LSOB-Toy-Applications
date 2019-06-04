import authenticated_requests
from league_ids import league_ids

yahoo_session = authenticated_requests.oauth_session()

year = 2019
request = "https://fantasysports.yahooapis.com/fantasy/v2/league/{}.l.{}/standings"\
    .format(league_ids[year]['game_id'], league_ids[year]['league_id'])
print(request)

response = authenticated_requests.make_auth_query(yahoo_session, request)
print(response['fantasy_content']['league']['standings']['teams'])