from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print(f"IP Packet: {packet[IP].src} -> {packet[IP].dst}")

def main():
    print("Starting packet capture...")
    sniff(filter="ip", prn=packet_callback, store=0)

if __name__ == "__main__":
    main()