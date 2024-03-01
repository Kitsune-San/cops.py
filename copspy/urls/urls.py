"""
Basic API url endpoints.

"""

import requests
current_version = requests.get("http://backend.yokaigroup.gg/copsapi/version")
number = current_version.json()




base_api_uri = f"https://{number}.prod.copsapi.criticalforce.fi/api/public"

username_api_uri = f"https://{number}.prod.copsapi.criticalforce.fi/api/public/profile?usernames="

id_api_url  = f"https://{number}.prod.copsapi.criticalforce.fi/api/public/profile?ids="