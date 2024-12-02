# Annexure: Zigbee PRO 2023 dynamic link key negotiation

There are two types of DLK negotiations. When the requester of a new TCLK is not yet authorized in the network \(does not have the network key\), the process is called off-network DLK negotiation. This occurs after the parent replies with the Network Commissioning Response. Once a node is fully joined and authorized, it can request a new TCLK from the trust center. If both nodes, the TC and the requester, supports DLK, they shall use the on-network DLK Negotiation method instead of the Zigbee 3.0 Request Key method. The on-network DLK can be triggered using the Node Descriptor request from the initiator to the trust center. The stack appends the Supported Key Negotiation method TLV to the request and the response contains the Selected Key Negotiation method TLV. If the Trust Center approved the DLK, the stack of the initiator initiates the key negotiation process.

The coordinator R23 and Router R23 examples contain code which activates the DLK, off- and on-network. The code is provided for experimentation as the DLK feature set is not fully implemented nor tested. It is enabled by changing the following macro:

```
**\#ifdef** R23_UPDATES 
/* Uncomment this to enable DLK with AES-128 */
//#define R23_DLK_AES128_ENABLE 1
**\#endif**
```

## AIB attributes

The AIB attribute `apsSupportedKeyNegotiationMethods` is a bit mask, which indicates the set of supported key negotiation methods by the local device. The set of valid values corresponds to the Supported Key Negotiation Methods Global TLV, which can be found in the `ZigbeeCommon/Include/tlv.h` file. Only the Hash AES-MMO-128 method is supported in this experimental preview.

```
**\#define** ZPS_TLV_G_SUPPKEYNEGMETH_STATKEYREQ  (1) /* Zigbee 3.0 Mechanism */
**\#define** ZPS_TLV_G_SUPPKEYNEGMETH_SPEKEAES128 (2) /* SPEKE using Curve25519 with Hash AES-MMO-128 */
**\#define** ZPS_TLV_G_SUPPKEYNEGMETH_SPEKESHA256 (4) /* SPEKE using Curve25519 with Hash SHA-256 */
```

At a minimum the device SHALL support one method, the key request method.

The AIB attribute `u8SharedSecretsMask` is a bit mask which indicates the set of supported shared secrets by the local device. The set of valid values corresponds to the supported key negotiation methods global TLV, which can be found in the `ZigbeeCommon/Include/tlv.h` file. Only the values \(1\) and \(4\) are supported, together with the default `apscWellknownPSK`.

```
**\#define** ZPS_TLV_G_PSK_SYMMETRIC    (1) /* Symmetric authentication token */
**\#define** ZPS_TLV_G_PSK_INSTALLCODE  (2) /* Pre-configured link-ley derived from installation code */
**\#define** ZPS_TLV_G_PSK_PASSCODE     (4) /* Variable-length pass code (for PAKE protocols) */
**\#define** ZPS_TLV_G_PSK_BASICAUTH    (8) /* Basic Authorization Key */
**\#define** ZPS_TLV_G_PSK_ADMINAUTH   (16) /* Administrative Authorization Key */
```

Setting these attributes in the AIB is done using the API `ZPS_teStatus ZPS_eAplAibSetKeyNegotiationOptions(uint8 u8Methods, uint8 u8SharedSecrets)`. The return value is always `ZPS_E_SUCCESS`.

## Joiner TLVs 

The device wanting to join an R23 network shall send the Network Commissioning Request command communicates information to the parent device with the Joiner TLVs directly in the message. The device shall include the Joiner Encapsulation Global TLV. In a multi-hop joining scenario the Trust Center and parent device will not be the same entity. Information about the sending device is communicated to the Trust Center through the Joiner Encapsulation Global TLV, which will be relayed in its entirety in the Update Device message. When a device creates the Joiner Encapsulation Global TLV it shall contain the following TLVs inside it:

Fragmentation Parameters Global TLV

If the device is not rejoining: Supported Key Negotiation Methods Global TLV

The Router R23 example contains the following code to set the Joiner TLVs before calling the stack initialization. These TLVs will be used by the stack as additional payload in the joining command. Their content is configured independently from the AIB attributes configuring the local node’s key negotiation options.

```
TLV_ENCAPS(g_sJoinerTlvs,
           APP_SIZE_JOINREQ_TLV,
           m_, tuTlvTestSpecific1,
           m_, tuFragParams,
           m_, tuSupportedKeyNegotiationMethods,
           m_, tuTlvTestSpecific2) =
{
        .u8Tag = ZPS_TLV_G_JOINERENCAPS, .u8Len = APP_SIZE_JOINREQ_TLV - 1,

        /* This TLV is sent inside the Joiner Encapsulation */
        { .u16ZigbeeManufId = 0x1234, .au8Extra[0] = 0xAA, .au8Extra[1] = 0xBB,
          .u8Tag = ZPS_TLV_G_MANUFSPEC, .u8Len = sizeof(tuTlvTestSpecific1) - 1 - ZPS_TLV_HDR_SIZE
        },

        { .u16NodeId = 1, .u8FragOpt = 2, .u16InMaxLen = 10,
          .u8Tag = ZPS_TLV_G_FRAGPARAMS, .u8Len = sizeof(tuFragParams) - 1 - ZPS_TLV_HDR_SIZE
        },

        { .u8KeyNegotProtMask = ZPS_TLV_G_SUPPKEYNEGMETH_STATKEYREQ
                                | R23_DLK_KEY_PROTO_NEGOTIATION_MASK,
          .u8SharedSecretsMask = R23_DLK_SHARED_SECRETS_MASK,
        ),
```

