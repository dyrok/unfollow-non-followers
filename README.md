# 🤖 Instagram Unfollow Bot (Safest F*cking Bot on the Internet) 🔄

The most paranoid, safety-obsessed Instagram unfollow bot that unfollows people who dont follow you back on instagram, that won't get your ass banned. Read every damn word below before using this.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1J_ZPd4jPHfbRgWeYroOaPNhMWR7ip5W3?usp=sharing)
[![GitHub](https://img.shields.io/github/license/dyrok/unfollow-non-followers?color=blue)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 🌟 Features Your Mom Would Approve Of

- ⏲️ Configurable delays (because Instagram WILL notice if you go too fast)
- 🔒 Session persistence (so you don't look sus logging in repeatedly)
- 📲 2FA support (for you security nerds)
- 🎲 Randomized unfollow order (f*ck patterns)
- 📊 Detailed logging (so you know exactly when you screwed up)
- ⚠️ Rate limit detection (with automatic pussy mode)
- 🛡️ Progressive delays (gets slower as you go)

## ☠️ Before You Start (READ THIS SH*T)

1. **Backup your following list** (Screenshot it or use `cl.user_following()`)
2. **Turn off all other Instagram activity** (No likes, no comments, no nothing)
3. **Use a dummy account first** (Unless you like living dangerously)
4. **Don't be greedy** (See the ramp-up schedule below)

## 🚀 Installation (Choose Your Weapon)

### Method 1: Google Colab (Easiest)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1J_ZPd4jPHfbRgWeYroOaPNhMWR7ip5W3?usp=sharing)

1. Click the Colab button above
2. Run the first two code blocks to install dependencies:
   ```python
   !pip install instagrapi
   !pip install pillow
   ```
3. Edit the credentials in the third block:
   ```python
   USERNAME = "your_instagram_username"  # No shit
   PASSWORD = "your_instagram_password"  # Duh
   ```
4. Run the remaining blocks

### Method 2: Local Installation (For Pros)
```bash
git clone https://github.com/dyrok/unfollow-non-followers.git
cd unfollow-non-followers
pip install -r requirements.txt
python main.py
```

## ⚠️⚠️⚠️ Ramp-Up Schedule (OR GET BANNED) ⚠️⚠️⚠️

Day | Max Unfollows | Notes
--- | --- | ---
1 | 25 | Baby steps, bitch
2 | 50 | Still warming up
3 | 75 | Getting there
4 | 100 | Now we're talking
5 | 125 | You're pushing it
6+ | 150-200 | Absolute madlad territory

**IMPORTANT:** During this period DO NOT:
- Like posts
- Comment
- Follow anyone
- Change your bio
- Basically exist on Instagram

## 🖥️ Usage Examples

### Newbie Mode (Recommended)
```bash
python main.py
How many people do you want to unfollow? 25  # Day 1 limit
```

### Custom Delays (For Paranoids)
```bash
python main.py
How many people do you want to unfollow? 50

Configure delays (in seconds):
  Minimum delay between API requests (default 2): 5
  Maximum delay between API requests (default 3): 10
  Minimum delay between unfollow actions (default 5): 30
  Maximum delay between unfollow actions (default 15): 60
```

### Max Safety Settings (For Pussies)
```python
API delays: 10-15 seconds
Unfollow delays: 60-120 seconds
Daily limit: ≤ 50 actions
```

## 💀 Common Ways to Get Banned

1. Running this while also using your phone
2. Going over daily limits
3. Not using delays
4. Being impatient
5. Not reading this guide

## 🩹 Troubleshooting

### "Please wait a few minutes"
- You went too fast, dumbass
- Wait at least 1 hour before trying again
- Reduce your unfollow count next time

### Login Challenges
1. Verify on your phone first
2. Wait 24 hours
3. Try again with slower settings

### Other Errors
```bash
pip install --upgrade instagrapi pillow
```

## 📄 License
MIT License - meaning I'm not responsible when you inevitably fuck up your account.

---

**Final Warning**: This is the internet equivalent of defusing a bomb while drunk. You've been warned.
