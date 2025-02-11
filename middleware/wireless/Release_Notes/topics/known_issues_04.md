# Known issues {#topic_ac293e3f-be63-47b1-9975-308b89b4e555}

|Component|Description|
|-----------|-------------|
|Bluetooth|<ul><li>Packet lost would be observed in CIS case which causes audio noise.</li><li>Sequential Removal of CIS Handles as per current Controller implementation i.e CIS Disconnection sequence should be in sequence =\> CIS - 4,3,2,1</li><li>While 4-CIS streaming, audio glitches observed on all CIS SINK with Samsung Galaxy buds</li><li>While 4-CIS streaming, disconnection with connection timeout observed on first CIS SINK with Samsung Galaxy buds</li><li>Only two streams \(CIS/BIS\) with one channel is supported.</li></ul>|

**Parent topic:**[AW611 release notes](../topics/aw611-release-notes.md)

