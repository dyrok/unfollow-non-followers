# 🤖 Instagram Unfollow Bot (Safest bot on the Internet) 🔄

A Python script that safely unfollows users who don't follow you back on Instagram, with configurable delays and anti-detection measures. Make sure you read the Entire Documentation before using this.

[![GitHub](https://img.shields.io/github/license/dyrok/unfollow-non-followers?color=blue)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 🌟 Features

- ⏲️ Configurable delays between actions (API requests and unfollows)
- 🔒 Session persistence for faster logins
- 📲 2FA (Two-Factor Authentication) support
- 🎲 Randomized unfollow order to avoid patterns
- 📊 Progress tracking and logging
- ⚠️ Safety mechanisms to prevent rate limiting
- 🛡️ Proxy-ready architecture (external configuration)

## 📋 Prerequisites

- Python 3.8+
- Instagram account credentials
- Basic terminal knowledge

```bash
# Required libraries
pip install instagrapi pillow
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/instagram-unfollow-bot.git
cd instagram-unfollow-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Edit the script to add your credentials:
```python
# At the bottom of the script
USERNAME = "your_instagram_username"  # 🚨 Replace this
PASSWORD = "your_instagram_password"  # 🚨 Replace this
```

## 🖥️ Usage

### Basic Usage
```bash
python unfollow_bot.py
```

### Custom Delays
```bash
python unfollow_bot.py
How many people do you want to unfollow? 50

Configure delays (in seconds):
  Minimum delay between API requests (default 2): 3
  Maximum delay between API requests (default 3): 5
  Minimum delay between unfollow actions (default 2): 10
  Maximum delay between unfollow actions (default 3): 15
```

### Max Safety Mode (Recommended)
```bash
# Slow settings for maximum stealth
API delays: 5-10 seconds
Unfollow delays: 30-60 seconds
Daily limit: ≤ 100 actions
```

## ⚠️ Important Notes

- 🔞 **Use at your own risk** - Automation violates Instagram's ToS
- ⏱️ **Rate Limits**: Max 500 actions/day (recommend ≤ 100) and if you youre using this thing for the first time, scoll to Usage guidlines, so you dont Ban your Instagram.
- 🛑 **Never run continuously** - Use in short sessions
- 📴 **Avoid simultaneous** device logins during operation
- 📈 **Monitor account status** regularly

## ⚠️⚠️⚠️ Usage Guide (Verry Important) ⚠️⚠️⚠️

During this Period DO NOT Like, Comment, Follow,  Change your bio or anything, every action you do counts as an activity. I am not responsible if you fuck your account up. If you do just remember that you were an absolute peice of shit who didnt wanna read documentation. (instagram may change these but these are just the best practice.)
   - On Day 1 Only unfollow **25 People**
   - On Day 2 Only unfollow **50 People**
   - On Day 3 Only unfollow **75 People**
   - On Day 4 Only unfollow **100 People**
   - On Day 5 Only unfollow **125 People**
   - ...... and so on if you want to reach 500 unfollows per day safely.

## 🛡️ Safety Recommendations

- 🔄 Mix with manual activity
- 🕒 Add random pauses (2-5 minutes) every 10-20 actions
- 📆 Spread unfollows over multiple days
- 💾 Backup your following list regularly
- 🧪 Test with a dummy account first

## 🐛 Troubleshooting

### Common Issues
1. **Login Challenges**:
   - Complete verification on mobile first
   - Wait 24-48 hours after suspicious activity

2. **Module Errors**:
   ```bash
   pip install --upgrade instagrapi pillow
   ```

3. **Rate Limits**:
   - Stop script immediately
   - Wait 24-48 hours before resuming

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer**: This script is for educational purposes only. The developers are not responsible for any account restrictions or bans resulting from its use. Use responsibly and at your own risk.

