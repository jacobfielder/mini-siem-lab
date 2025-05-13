# 🔐 Mini SIEM – SSH Log Monitor with Slack Alerts

A lightweight Python-based SIEM tool that monitors SSH logs, detects brute-force login attempts, and sends real-time alerts to Slack. Built as a practical cybersecurity/networking project to simulate a SOC analyst's detection logic.

---

## 📌 Features

- 🧠 Parses SSH login failures from `auth.log`
- 📊 Tracks failed login attempts per IP address
- 🚨 Alerts when an IP crosses a configurable threshold
- 💬 Sends real-time alerts to Slack via webhook
- 📂 Simple structure – easy to extend or integrate into other projects

---

## 🖼️ Demo

> 📷 Screenshot of alert in Slack (replace with your own)

## How the SIEM Works

- 1. Reads a log fole ('auth.log') line by line
- 2. Uses expressions to extract
	- Username
	- IP address
	- Port
- 3. Tracks failed logins per IP address
- 4. If an IP hits the threshold, it will:
	- Print to the console
	- Send an alert to a configured Slack channel

## 🧠 What I Learned

- How to parse Linux SSH logs using **Python**
- Building a simple **brute-force detection engine**
- Sending real-time **Slack alerts** using webhooks
- Gained more experience in the command line using **bash**
