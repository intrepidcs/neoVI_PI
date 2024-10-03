# Python API

### **Receive Messages** <a href="#a867" id="a867"></a>

Use this function to Receive CAN messages

```python
def receive_can(device):    
    msgs, error_count = ics.get_messages(device)
    print("Received {} messages with {} errors.".format(len(msgs), error_count))
    for i, m in enumerate(msgs):
       print('Message #{}\t'.format(i+1), end='')
       print('\tArbID: {}\tData: {}'.format(hex(m.ArbIDOrHeader), [hex(x) for x in m.Data]))
```

### Transmit Messages <a href="#id-632c" id="id-632c"></a>

Use this function to Transmit CAN messages

```python
def transmit_can(device):
    msg = ics.SpyMessage()
    msg.ArbIDOrHeader = 0x01 # CAN Arbitration ID
    msg.Data = (1,2,3,4,5,6,7,8) # Data Bytes go here
    msg.NetworkID = ics.NETID_HSCAN # First channel of CAN
        # msg parameter here can also be a tuple of messages
    ics.transmit_messages(device, msg)
```

<figure><img src="../.gitbook/assets/1_5X5idBlTMs-iMF7gUzLWNg.png" alt=""><figcaption></figcaption></figure>

You can read the full documentation for libicsneo at [https://libicsneo.readthedocs.io/en/latest/](https://libicsneo.readthedocs.io/en/latest/) and Python documentation at [https://python-ics.readthedocs.io/en/2.15/](https://python-ics.readthedocs.io/en/2.15/).
