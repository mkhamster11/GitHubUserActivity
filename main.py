import argparse
import json
from urllib.request import Request, urlopen
parser = argparse.ArgumentParser(description="github user activity finder")
parser.add_argument('username', type=str,help='please need git username',nargs=1)
args = parser.parse_args()


args.username

def get_activity(username="mkhamster11"):
    rp = Request(f"https://api.github.com/users/{username}/events?per_page=2&page=1",method="GET")
    with urlopen(rp) as response:
        return json.load(response)


data = get_activity("mkhamster11")
print(data)
print("Output:")
for i in data:
    print(i)
