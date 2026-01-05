# TL1 Client

A Python client for communicating with telecom equipment using the TL1 (Transaction Language 1) protocol.

## Overview

TL1 is an ASCII-based management protocol widely used in telecommunications for managing network elements like SONET/SDH equipment, DSLAM, and optical transport systems.

## Features

- TCP socket-based TL1 connection
- Configurable timeout
- Automatic command termination (semicolon)
- Response parsing with TL1 prompt detection

## Usage

```python
from tl1_client import TL1Client

client = TL1Client("192.168.1.100", 3083)
client.connect()

# Retrieve header information
response = client.send_command("RTRV-HDR:::1234")
print(response)

# Retrieve all alarms
response = client.send_command("RTRV-ALM-ALL:::5678")
print(response)

client.close()
```

## Common TL1 Commands

| Command | Description |
|---------|-------------|
| `RTRV-HDR` | Retrieve header/system info |
| `RTRV-ALM-ALL` | Retrieve all alarms |
| `RTRV-INV` | Retrieve inventory |
| `ACT-USER` | Activate/login user |
| `CANC-USER` | Cancel/logout user |

## Configuration

- **Host**: IP address of the TL1-enabled device
- **Port**: TL1 port (commonly 3083 or 3082)
- **Timeout**: Connection and response timeout in seconds

## Requirements

- Python 3.x
