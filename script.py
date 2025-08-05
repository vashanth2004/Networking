import psutil
import time
import datetime
import csv
import os

def get_size(bytes):
    for unit in ['', 'K', 'M', 'G']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024
    return f"{bytes:.2f}TB"

def log_to_file(timestamp, upload, download, interface, connections):
    with open("network_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | Interface: {interface} | Upload: {upload}/s | Download: {download}/s\n")
        for conn in connections:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            try:
                proc_name = psutil.Process(conn.pid).name()
            except:
                proc_name = "N/A"
            f.write(f"    - Process: {proc_name} | Local: {laddr} | Remote: {raddr} | Status: {conn.status}\n")

def log_to_csv(timestamp, upload, download, interface, connections):
    file_exists = os.path.isfile("network_log.csv")
    with open("network_log.csv", "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow([
                "Timestamp", "Interface", "Upload", "Download",
                "Process", "Local Address", "Remote Address", "Status"
            ])
        for conn in connections:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            try:
                proc_name = psutil.Process(conn.pid).name()
            except:
                proc_name = "N/A"
            writer.writerow([timestamp, interface, upload, download, proc_name, laddr, raddr, conn.status])

def get_active_interface():
    net_stats = psutil.net_io_counters(pernic=True)
    return max(net_stats.items(), key=lambda x: x[1].bytes_recv + x[1].bytes_sent)[0]

def print_table(timestamp, upload, download, interface, connections):
    print("\n" + "="*80)
    print(f"{timestamp} | Interface: {interface}")
    print(f"{'Upload':<10}: {upload}/s")
    print(f"{'Download':<10}: {download}/s")
    print("-" * 80)
    print(f"{'Process':<25}{'Local Address':<25}{'Remote Address':<25}{'Status'}")
    print("-" * 80)
    for conn in connections:
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        try:
            proc_name = psutil.Process(conn.pid).name()
        except:
            proc_name = "N/A"
        print(f"{proc_name:<25}{laddr:<25}{raddr:<25}{conn.status}")
    print("="*80 + "\n")

print("📊 Starting Network Monitor... Press Ctrl+C to stop.")
try:
    interface = get_active_interface()
    print(f"Monitoring Interface: {interface}")
    while True:
        io_1 = psutil.net_io_counters(pernic=True)[interface]
        time.sleep(1)
        io_2 = psutil.net_io_counters(pernic=True)[interface]

        upload_speed = io_2.bytes_sent - io_1.bytes_sent
        download_speed = io_2.bytes_recv - io_1.bytes_recv

        upload = get_size(upload_speed)
        download = get_size(download_speed)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        connections = psutil.net_connections(kind='inet')
        print_table(timestamp, upload, download, interface, connections)
        log_to_file(timestamp, upload, download, interface, connections)
        log_to_csv(timestamp, upload, download, interface, connections)

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped.")
except Exception as e:
    print(f"\n⚠️ Error: {e}")
