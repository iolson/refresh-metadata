# Built with Python 3, dependencies installed with pip3

import sys
import requests

openseaDefaultUrl = 'https://api.opensea.io/asset/{CONTRACT_ADDRESS}/{TOKEN_ID}?force_update=true'
raribleDefaultUrl = 'https://api.rarible.com/marketplace/api/v4/items/{CONTRACT_ADDRESS}%3A{TOKEN_ID}/meta/refresh'

if (len(sys.argv) < 4):
    print('Not enough arguments passed in for refresh of metadata.')
    quit()

contractAddress = sys.argv[1]
tokenId = int(sys.argv[2])
totalTokens = int(sys.argv[3])

while (tokenId <= totalTokens):

    # OpenSea
    openseaUrl = openseaDefaultUrl.replace('{CONTRACT_ADDRESS}', contractAddress).replace('{TOKEN_ID}', str(tokenId))
    requests.get(url=openseaUrl)
    print('Token ID: ' + str(tokenId) + ' OpenSea Refresh Submitted')

    # Rarible
    raribleUrl = raribleDefaultUrl.replace('{CONTRACT_ADDRESS}', contractAddress).replace('{TOKEN_ID}', str(tokenId))
    requests.post(url=raribleUrl)
    print('Token ID: ' + str(tokenId) + ' Rarible Refresh Submitted')

    tokenId += 1