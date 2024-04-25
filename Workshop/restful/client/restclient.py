#!/usr/bin/env python3

import sys
import time
import requests

# parse command line arguments: restclient [host [port]]
#
if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = "localhost"

try:
    port = int(sys.argv[2])
except Exception:
    port = 8080

# prepare url
#
url = "http://" + host + ":" + str(port) + "/products"

# infinite loop to obtain all products
#
while True:
    # get all product id's as list
    resp = requests.get(url)

    # verify status code
    if resp.status_code != 200:
        sys.exit("Status", resp.status_code, "for URL", url)

    # for each product, obtain details
    for productid in resp.json():
        produrl  = url + "/" + str(productid)
        prodresp = requests.get(produrl)

        if prodresp.status_code != 200:
            sys.exit("Status", prodresp.status_code, "for URL", produrl)

        product = prodresp.json()   # convert to Python dict

        print("Product {0[id]:>3}: {0[name]:<10} {0[description]}".format(product), flush=True)

    print()
    time.sleep(1)

sys.exit(0)
