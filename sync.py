#!/usr/bin/env python3

import requests


latest_gfwlist = "latest-gfwlist.txt"


def download_latest_gfwlist():
    url = "https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
    resp = requests.get(url)
    content = resp.text
    with open(latest_gfwlist, "wt") as fp:
        fp.write(content)
    print(f"{latest_gfwlist} saved")


def main():
    download_latest_gfwlist()


if __name__ == '__main__':
    main()
