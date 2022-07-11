## wireshark

Wireshark capture
```tcpdump -i interface -U -s0 -w - 'tcp and not port 22' | wireshark -k -i - ```

- https://github.com/welchbj/ctf/blob/master/docs/pcap.md
- file extraction: https://www.sneakymonkey.net/2017/03/03/pcap-file-extraction/
- WireShark webpage for common vulns

- MITM attacks
- ARP poisoning
