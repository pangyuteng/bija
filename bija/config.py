DEFAULT_RELAYS = [
    'wss://nostr.drss.io',
    'wss://nostr-pub.wellorder.net',
    'wss://nostr-relay.wlvs.space',
    'wss://nostr.bitcoiner.social',
    'wss://nostr-pub.semisol.dev',
    'wss://relay.damus.io	'
]

import os
import sys
import json

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
EXTENDED_JSON_FILE = os.path.join(THIS_DIR,'relays.json')

if os.path.exists(EXTENDED_JSON_FILE):
    with open(EXTENDED_JSON_FILE,'r') as f:
        my_list = json.loads(f.read())
        my_list = list(set(my_list))
    DEFAULT_RELAYS.extend(my_list)

