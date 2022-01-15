import dpkt

input_file = open("input_file.pcap", "rb")
pcap = dpkt.pcap.Reader(input_file)

output_file = open("out", "wb")

for timestamp, buf in list(pcap)[1:]:

	eth = dpkt.ethernet.Ethernet(buf)
	ip = eth.data
	icmp = ip.data
	output_file.write(icmp.data.data)

input_file.close()
output_file.close()
