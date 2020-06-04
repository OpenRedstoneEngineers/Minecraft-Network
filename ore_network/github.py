import requests
import json

base_url = "https://api.github.com"


def get_releases(owner, repo):
    endpoint = "/repos/{owner}/{repo}/releases"
    r = requests.get(base_url + endpoint.format(owner=owner, repo=repo))
    if r.ok:
        return json.loads(r.text or r.content)
    else:
        raise FileNotFoundError("API error")


def get_asset(owner, repo, release_name, content_type):
    print(owner, repo, release_name, content_type)
    releases = get_releases(owner, repo)
    for release in releases:
        if release["name"] == release_name:
            for asset in release["assets"]:
                if asset["content_type"] == content_type:
                    return asset["name"], asset["browser_download_url"]
    raise FileNotFoundError("Release asset was not found")
