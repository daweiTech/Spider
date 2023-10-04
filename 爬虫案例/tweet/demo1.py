import requests


headers = {
    "authority": "twitter.com",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": "^\\^",
    "x-twitter-client-language": "en",
    "x-csrf-token": "289c9e9c1c3c3321072cd83e142d6cc9f2e0c8978b95dfb2cef26385e733cb4aeb49f03dc625316ad17d4057b8d0c49324a6a62509a5eee82cc7c1365213866c0cfa83af2f2aed78a7a4c8ab1ab60f5b",
    "sec-ch-ua-mobile": "?0",
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs^%^3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "x-twitter-auth-type": "OAuth2Session",
    "x-twitter-active-user": "yes",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://twitter.com/NBAMemes/status/1587641118748856320",
    "accept-language": "zh-CN,zh;q=0.9"
}
cookies = {
    "personalization_id": "^\\^v1_tXxUAe0dcDz7uK2IlQaqkA==^^",
    "guest_id_marketing": "v1^%^3A166305753887075679",
    "guest_id_ads": "v1^%^3A166305753887075679",
    "guest_id": "v1^%^3A166305753887075679",
    "_ga": "GA1.2.172042981.1663057543",
    "mbox": "session^#0fbc41968bf34d76bf4a627483b7c847^#1663059600^|PC^#0fbc41968bf34d76bf4a627483b7c847.38_0^#1726302540",
    "g_state": "^{^\\^i_l^^:0^}",
    "kdt": "1GXpETTlStoewYrZ1IQdxwFio060p7eICjqimSgd",
    "auth_token": "e8bab11c746f315132f4008b94ab391170c1d6f1",
    "twid": "u^%^3D1574774248236666880",
    "ct0": "289c9e9c1c3c3321072cd83e142d6cc9f2e0c8978b95dfb2cef26385e733cb4aeb49f03dc625316ad17d4057b8d0c49324a6a62509a5eee82cc7c1365213866c0cfa83af2f2aed78a7a4c8ab1ab60f5b",
    "dnt": "1",
    "external_referer": "padhuUp37zhD6^%^2F29CpQtyhGQCUl05AFo^|0^|8e8t2xd8A2w^%^3D",
    "_gid": "GA1.2.1251012114.1667393815"
}
url = "https://twitter.com/i/api/graphql/lwMlLKa0uCr-By_siQJaGQ/TweetDetail"
params = {
    "variables": "^%^7B^%^22focalTweetId^%^22^%^3A^%^221587641118748856320^%^22^%^2C^%^22cursor^%^22^%^3A^%^22QAAAAPEDHBlmgoCwtfHut4gsgICwsenkCQBBstGu3wkAQKOxpecJAPAJwKLt3M63iCyEgLy9k-e3iCwlAhIVBAAA^%^22^%^2C^%^22referrer^%^22^%^3A^%^22tweet^%^22^%^2C^%^22controller_data^%^22^%^3A^%^22DAACDAAFDAABDAABDAABCgABAAAAAAAAgEAAAAwAAgoAAQAAAAAAAAAhCgACiGIkAxieiM0LAAMAAAADTkJBCgAFYjdgUT55L5kIAAYAAAABAAAAAAA^%^3D^%^22^%^2C^%^22with_rux_injections^%^22^%^3Afalse^%^2C^%^22includePromotedContent^%^22^%^3Atrue^%^2C^%^22withCommunity^%^22^%^3Atrue^%^2C^%^22withQuickPromoteEligibilityTweetFields^%^22^%^3Atrue^%^2C^%^22withBirdwatchNotes^%^22^%^3Afalse^%^2C^%^22withSuperFollowsUserFields^%^22^%^3Atrue^%^2C^%^22withDownvotePerspective^%^22^%^3Atrue^%^2C^%^22withReactionsMetadata^%^22^%^3Afalse^%^2C^%^22withReactionsPerspective^%^22^%^3Afalse^%^2C^%^22withSuperFollowsTweetFields^%^22^%^3Atrue^%^2C^%^22withVoice^%^22^%^3Atrue^%^2C^%^22withV2Timeline^%^22^%^3Atrue^%^7D",
    "features": "^%^7B^%^22verified_phone_label_enabled^%^22^%^3Afalse^%^2C^%^22responsive_web_graphql_timeline_navigation_enabled^%^22^%^3Atrue^%^2C^%^22unified_cards_ad_metadata_container_dynamic_card_content_query_enabled^%^22^%^3Atrue^%^2C^%^22tweetypie_unmention_optimization_enabled^%^22^%^3Atrue^%^2C^%^22responsive_web_uc_gql_enabled^%^22^%^3Atrue^%^2C^%^22vibe_api_enabled^%^22^%^3Atrue^%^2C^%^22responsive_web_edit_tweet_api_enabled^%^22^%^3Atrue^%^2C^%^22graphql_is_translatable_rweb_tweet_is_translatable_enabled^%^22^%^3Atrue^%^2C^%^22standardized_nudges_misinfo^%^22^%^3Atrue^%^2C^%^22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled^%^22^%^3Afalse^%^2C^%^22interactive_text_enabled^%^22^%^3Atrue^%^2C^%^22responsive_web_text_conversations_enabled^%^22^%^3Afalse^%^2C^%^22responsive_web_enhance_cards_enabled^%^22^%^3Atrue^%^7D"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)