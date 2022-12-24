# Wireshark

* https://www.wireshark.org/docs/
* https://wiki.wireshark.org/SampleCaptures
* https://dfirmadness.com/case-001-pcap-analysis/

## Filtering

### Filetering Operators

* and - operator: and / &&
* or - operator: or / ||
* equals - operator: eq / ==
* not equal - operator: ne / !=
* greater than - operator: gt /  >
* less than - operator: lt / <
* https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html

### Basic Filtering
* https://wiki.wireshark.org/DisplayFilters
```
ip.addr == <IP Address>
```
```
ip.src == <SRC IP Address> and ip.dst == <DST IP Address>
```
```
tcp.port eq <Port #> or <Protocol Name>
```
```
eth.addr == <MAC Address>
```

## Automated Analysis

* NetworkMiner


#### References
* https://tryhackme.com/room/wireshark
