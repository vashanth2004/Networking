# 📡 Python Network Monitor

A real-time **network monitoring script** built using Python and `psutil`. It tracks upload/download speed and active network connections, and logs the data into both `.txt` and `.csv` formats.

---

## 🚀 Features

- 📈 Monitors real-time **upload and download speed**
- 🌐 Tracks **active network connections**
- 🧾 Logs data to:
  - `network_log.txt` (text format)
  - `network_log.csv` (structured CSV)
- 💡 Displays live data in terminal with clear tabular format
- 🔧 Auto-detects the most active network interface

---

## 🛠️ Requirements

- Python 3.x
- psutil

## 📦 Installation

Install the required Python package:

```bash
pip install psutil
```

---

## ▶️ How to Run

1. Save the code in a file named, for example, `network_monitor.py`.
2. Run it using the terminal or command prompt:

```bash
python network_monitor.py
```

3. Watch your terminal for live stats.
4. Check `network_log.txt` and `network_log.csv` in the same directory for saved logs.

---

## 🖥️ Sample Output (Terminal)

```
================================================================================
2025-08-05 14:30:12 | Interface: Wi-Fi
Upload    : 56.24KB/s
Download  : 190.48KB/s
--------------------------------------------------------------------------------
Process                 Local Address            Remote Address           Status
--------------------------------------------------------------------------------
chrome.exe              192.168.0.102:53134      172.217.194.188:443      ESTABLISHED
python.exe              192.168.0.102:65432      192.168.0.1:53           TIME_WAIT
...
================================================================================
```

---

## 📁 Log Files

- `network_log.txt`: Human-readable log
- `network_log.csv`: Structured log for analysis in Excel, Power BI, etc.

---

## 📌 Notes

- The script refreshes every second.
- You can stop it anytime using `Ctrl+C`.
- Logs are appended each second, so make sure to manage file size for long runs.

---

## 📚 Use Cases

- Network traffic analysis for developers or sysadmins
- Internet usage monitoring on shared/public computers
- Educational projects in Python system programming

---

## 🔒 Disclaimer

This tool only accesses public process and socket information using `psutil`. It does **not** access any private content or payload data.

---

## 🤝 Contributions

Feel free to fork and improve the tool! You could add:
- Real-time web dashboard (Flask)
- Historical graph reports
- Bandwidth usage alerts
