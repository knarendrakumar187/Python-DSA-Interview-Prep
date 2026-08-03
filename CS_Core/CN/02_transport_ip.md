# CN 02 — IP, TCP vs UDP, Transport basics

## IP addressing
IP = device address on network.  
IPv4 example: `192.168.1.1`  
IPv6 = longer, more addresses.

## TCP vs UDP (top question)
| | TCP | UDP |
|--|-----|-----|
| Reliability | yes (ack, retransmit) | no |
| Order | ordered | not guaranteed |
| Speed | slower | faster |
| Use | web, file, email | video call, gaming, DNS often |

## TCP handshake (3-way)
SYN → SYN-ACK → ACK  
Then data transfer.

## Congestion control (1 line)
TCP slows down when network is overloaded.

## MAC address
Hardware address of NIC (local network identity).

## Speak answer
> TCP is connection-oriented and reliable; UDP is lightweight and faster but unreliable. File download needs TCP; live streaming can use UDP.

## Practice
When would you choose UDP over TCP?
