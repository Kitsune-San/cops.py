import requests
from copspy import api_urls
from requests.exceptions import ConnectionError as cnerr
from copspy.apierror import NoNetwork, ResponseNotOK

headers = {
    "content-type": "application/json",
}

all_servers = [
    1,
    2,
    7,
    8,
    11,
    12,
    13,
    15,
    17,
    18,
    20,
    22,
    23,
    24,
    25,
    27,
    31,
    32,
    36,
    38,
    50,
    51,
    53,
    54,
    57,
    66,
    71,
    72,
    74,
    75,
    76,
    77,
    79,
    80,
    81,
    84,
    85,
    98,
]


def get_all():
    """Get a list of all servers. Returns in json format."""
    try:
        json_servers = requests.get(api_urls.servers_api_url, headers=headers)
        if json_servers.ok:
            return json_servers.json()
        else:
            raise ResponseNotOK()
    except cnerr:
        raise NoNetwork()
