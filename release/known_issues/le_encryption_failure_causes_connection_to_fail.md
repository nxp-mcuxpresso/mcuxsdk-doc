# LE encryption failure causes connection to fail 

There can be a corner case when LE link encryption can fail. This occurs when device under test \(DUT\); RT Bluetooth controller here, while waiting for the response to LL\_SLAVE\_FEATURES\_REQ, instead receives the LL\_ENC\_REQ response from a remote device.

This causes deadlock scenario where DUT and remote devices are stuck waiting for response from peer.


