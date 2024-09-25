from scapy.all import sniff
from pymongo import MongoClient
from collections import Counter
import signal
import sys

# MongoDB connection
client = MongoClient('mongodb://mongo:27017/')
db = client['packet_db']
collection = db['packets']

# statistic envs
packet_count = 0
protocols = Counter()
src_ips = Counter()
dst_ips = Counter()

# function to get packets
def packet_callback(packet):
    global packet_count

    # check if packet has a IP
    if packet.haslayer('IP'):
        packet_count += 1

        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        proto = packet['IP'].proto
        packet_size = len(packet)

        # update statistics
        protocols[proto] += 1
        src_ips[src_ip] += 1
        dst_ips[dst_ip] += 1

        # saves on MongoDB
        packet_data = {
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'protocol': proto,
            'size': packet_size
        }
        collection.insert_one(packet_data)

# function to show statistics
def print_statistics():
    print(f"\nTotal number of packets captured: {packet_count}")
    print(f"Number of packets per protocol: {protocols}")

    print("\nTop 5 source IPs with the most traffic:")
    for ip, count in src_ips.most_common(5):
        print(f"{ip}: {count} packets")

    print("\nTop 5 destination IPs with the most traffic:")
    for ip, count in dst_ips.most_common(5):
        print(f"{ip}: {count} packets")

# function to stop packets capture
def stop_sniffing(signum, frame):
    print("\nStop capture...")
    print_statistics()
    sys.exit(0)

# configure interruption signal
signal.signal(signal.SIGINT, stop_sniffing)

if __name__ == "__main__":
    # network interface
    interface = "eth0"
    print(f"Capturing packets from interface {interface}... (press Ctrl+C to interrupt)")

    # starts packets capture
    sniff(iface=interface, prn=packet_callback)
