## 🌟 How to Create an Account on Serv00.com and Deploy a Telegram Bot Using SSH (Free Plan)

This guide will walk you through the steps of creating a **free account** on **Serv00.com**, setting up **SSH access**, and deploying a **Telegram bot** using the free hosting plan. Let's dive in! 🛠️

If this guide helps you, please consider following me on [GitHub](https://github.com/Harshit-shrivastav) 😊!

---

### 📝 Step 1: Create an Account on Serv00.com

#### 1.1 🌐 Visit Serv00.com

1. Open your web browser and go to [Serv00.com](https://serv00.com).
2. You'll land on the homepage of the **free hosting provider**.

#### 1.2 🆕 Register for a Free Account

1. Click on the **Sign Up** or **Register** button.
2. Fill out the form with:
   - **📛 Full Name**
   - **✉️ Email Address**
   - **🔑 Username**
   - **🔒 Password**
   
3. Verify your email by clicking the link in the confirmation email sent to your inbox.

#### 1.3 🏗️ Choose a Free Hosting Plan

1. Log in to the **Serv00 dashboard** after verifying your account.
2. Choose the **Free Hosting Plan**.
3. Once activated, you’ll have access to your **hosting dashboard** where you can set up your bot.

---

### 🔐 Step 2: Retrieve SSH Access Credentials

1. In your Serv00 dashboard, go to the **Server Information** section.
2. Find the following important details:
   - **🌐 Hostname** or **IP Address**
   - **👤 SSH Username**
   - **🔑 SSH Password**
   - **🔌 Port Number** (typically `22`)

---

### 💻 Step 3: Set Up Termius and Log in via SSH

We'll use **Termius** for easy SSH access to your server. It's a user-friendly SSH client available on multiple platforms.

#### 3.1 📥 Download and Install Termius

1. Head to [Termius.com](https://termius.com) and download the app for your platform (Windows, macOS, Linux, Android, or iOS).
2. Install and launch **Termius**.

#### 3.2 🔌 Configure SSH in Termius

1. Click on **Hosts** in the Termius menu.
2. Click the **"+"** button to add a new SSH host.
3. Fill in the following details:
   - **📌 Label (Name):** Name the connection (e.g., "Serv00 Server").
   - **🌐 Hostname:** The server's **IP address** or **domain**.
   - **🔌 Port:** `22` (or the port provided by Serv00).
   - **👤 Username:** The **SSH username** from the dashboard.
   - **🔑 Password:** Your **SSH password** from the dashboard.

4. Click **Save**, then click on your saved host to connect.

Once connected, you will enter the server terminal via SSH. Now let's deploy your bot! 🤖

---

### 🤖 Step 4: Deploy a Basic Telegram Bot

#### 4.1 🐍 Install Python and Required Libraries

Run the following commands to install **Python** and the `python-telegram-bot` library:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install python-telegram-bot
```

#### 4.2 📄 Create the Telegram Bot Script

1. Create a new file called `my_bot.py` using a text editor like **nano**:

```bash
nano my_bot.py
```

2. Paste the following basic bot code:

```python
from telegram.ext import Updater, CommandHandler

# Replace with your actual bot token from BotFather
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update, context):
    update.message.reply_text('Hello! Welcome to the bot.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

👉 Don't forget to **replace** `'YOUR_TELEGRAM_BOT_TOKEN'` with the token from **[BotFather](https://core.telegram.org/bots#botfather)**.

3. Save the file and exit the editor (`Ctrl + O`, `Enter`, `Ctrl + X`).

#### 4.3 🚀 Run Your Bot

Run the bot using Python:

```bash
python3 my_bot.py
```

Your Telegram bot is now running! 🥳 You can start chatting with it by sending the `/start` command in Telegram.

---

### ⚙️ Step 5: Keep the Bot Running

You don't want your bot to stop when you close your SSH session, right? Use one of the following methods to keep it running:

#### Option 1: Using `screen` 🖥️

1. Install screen:

```bash
sudo apt install screen
```

2. Start a screen session:

```bash
screen -S my_bot
```

3. Run your bot:

```bash
python3 my_bot.py
```

4. Detach the screen (`Ctrl + A + D`), and your bot will keep running in the background.

#### Option 2: Using `nohup` 💡

Run your bot in the background using `nohup`:

```bash
nohup python3 my_bot.py &
```

Now, your bot will keep running even after you log out of the SSH session!

---

### 🎉 Conclusion

Congratulations! You've successfully created an account on **Serv00.com**, logged in using SSH with Termius, and deployed a basic Telegram bot. Now you're all set to expand and build on your bot! 🚀

If this article helped you, please consider following me on [GitHub](https://github.com/Harshit-shrivastav) for more tutorials and projects! 💻👨‍💻
