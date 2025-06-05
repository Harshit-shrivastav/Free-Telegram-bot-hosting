import json

try:
    with open("hosts.json", "r", encoding="utf-8") as f:
        hosts = json.load(f)
except FileNotFoundError:
    print("❌ Error: hosts.json file not found")
    exit(1)
except json.JSONDecodeError:
    print("❌ Error: Invalid JSON in hosts.json")
    exit(1)

# Sort hosts case-insensitively by name
hosts.sort(key=lambda x: x.get("name", "").lower())

# Counters for platform statuses
total_count = len(hosts)
working_count = partial_count = not_working_count = 0

# Generate markdown table
table_md = "| 🌐 Platform | ✅ Status | 💬 Remark |\n"
table_md += "|------------|-----------|-----------|\n"

for host in hosts:
    name = host.get("name", "N/A")
    url = host.get("url", "")
    status = host.get("status", "").strip().lower()
    remark = host.get("remark", "")

    # Determine status emoji and update counters
    if status == "working":
        status_emoji = "🟢 Working"
        working_count += 1
    elif status == "partial":
        status_emoji = "🟡 Partial"
        partial_count += 1
    else:
        status_emoji = "🔴 Not Working"
        not_working_count += 1

    # Create platform name with link if URL exists
    platform_display = f"[{name}]({url})" if url else name

    # Add row to table
    table_md += f"| {platform_display} | {status_emoji} | {remark} |\n"

# Generate summary badge
summary_badge = f"🟢 {working_count} | 🟡 {partial_count} | 🔴 {not_working_count} — **Total: {total_count}**"

# Generate README content
readme = f"""# 🚀 Free Telegram Bot Hosting Platforms

Looking for free Telegram bot hosting? Here's a curated list of platforms with live status checks!

> 💳 **No credit-card required:** Every platform listed here grants free credits *without* needing a card or any payment verification. 


> ⚠️ **Note:** Free platforms may have usage limits (uptime, memory, storage, etc.).  


> ⚙️ **Always double-check** current policies before using any service.

---

## 📊 Hosting Status Summary

{summary_badge}

---

## 📋 Hosting Status Table

{table_md}

---

## 🤝 Contribute

Want to improve this list?  
Check out [`CONTRIBUTING.md`](CONTRIBUTING.md) to learn how you can help!

Update `hosts.json` and send a PR 💡

---

## ⭐ Star the Repo

If you found this useful, please consider [starring the repo](https://github.com/Harshit-shrivastav/telegram-bot-hosts) to show your support!

---

## 🔗 Follow Me

Stay connected for more such open-source utilities & updates!  
[![Follow](https://img.shields.io/github/followers/Harshit-shrivastav?style=social)](https://github.com/Harshit-shrivastav)

---

## 📬 Contact Me

Got suggestions, improvements, or just want to chat?

- 💬 **Telegram:** [@IzHarshit](https://telegram.me/izharshit)  
- 📧 **Email:** i@h-s.site

---

Made with ❤️ by [Harshit Shrivastav](https://github.com/Harshit-shrivastav)
"""

# Write README.md
try:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print("✅ README.md successfully generated.")
except IOError as e:
    print(f"❌ Error writing README.md: {e}")
