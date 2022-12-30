DEFAULT_RELAYS = [
    'wss://nostr.drss.io',
    'wss://nostr-pub.wellorder.net',
    'wss://nostr-relay.wlvs.space',
    'wss://nostr.bitcoiner.social',
    'wss://nostr-pub.semisol.dev',
    'wss://relay.damus.io	'
]

import json
if os.path.exists('relays.json'):
    with open('relays.json','r') as f:
        mylist = json.loads(f.read())
    DEFAULT_RELAYS.extends(mylist)

