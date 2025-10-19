# 🕵️ GitHub User Activity CLI

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-stalking%20legally-brightgreen)

> **"With great power comes great responsibility... "**



## 🚀 Quick Start (For the Impatient)

### Prerequisites

- Python 3.6+ (If you're still on Python 2, we need to have a talk)
- Internet connection (Duh!)
- A GitHub username to research

### Installation

```bash
# Clone this bad boy
git clone https://github.com/yourusername/github-activity.git
cd github-activity

# Make it executable (Unix/Linux/Mac)
chmod +x github-activity.py

# Run it!
python github-activity.py <username>
```

### Example Usage

```bash
# See what the legendary Linus Torvalds is up to
python github-activity.py torvalds

# Check on your coding idol
python github-activity.py kamranahmedse

# Stalk yourself (no judgment here)
python github-activity.py your-username
```



## 🎪 How It Works 

1. **You** type a username (the easy part)
2. **The script** politely asks GitHub's API for recent activity
3. **GitHub** responds with a JSON blob (because who doesn't love JSON?)
4. **We** parse that JSON faster than you can say "undefined is not a function"
5. **Your terminal** displays beautiful, formatted activity
6. **You** feel like a hacker from a 90s movie

### Under the Hood 🔧

This project uses:
- `urllib.request` - Because we're hardcore and don't need `requests`
- `json` - For parsing GitHub's data buffet
- `sys` - For that sweet command-line argument handling
- `datetime` - Because timestamps are important, people!

**No pip install required!** This is 100% Python standard library. 

## 🛠️ Advanced Usage (For the Overachievers)

### Common Use Cases

**Scenario 1: The Job Interview Prep**
```bash
# Research the company's developers before your interview
python github-activity.py company-dev-username
```

**Scenario 2: Open Source Reconnaissance**
```bash
# See if a maintainer is active before opening an issue
python github-activity.py maintainer-username
```

**Scenario 3: Competitive Analysis**
```bash
# See what your competitors are building
python github-activity.py competitor-username
```

**Scenario 4: Pure Curiosity**
```bash
# What is DHH up to these days?
python github-activity.py dhh
```

### Pro Tips 💡

- GitHub API has rate limits (60 requests/hour without auth). Don't go crazy!
- The tool shows the 10 most recent activities by default
- Timestamps are in UTC 


## 🐛 Troubleshooting (When Things Go Wrong)

### "Error: User 'xxxx' not found"
Either you misspelled the username, or that user is so underground they don't exist yet. Double-check the spelling!

### "Error: API rate limit exceeded"
You've been clicking too much! GitHub limits unauthenticated requests to 60/hour. Take a coffee break ☕

### "Network Error: ..."
Your internet is down. Or GitHub is down. Or the internet is down. Check your connection!

### "This doesn't work on Windows!"
It does! But you might need to use `python` instead of `./github-activity.py`. Windows is special like that.

## 🤝 Contribution

Found a bug? Want to add a feature? Have a hilarious error message to suggest? We accept PRs!



## 🎯 Roadmap (The Dream)

- [x] Basic functionality
- [x] Error handling that doesn't make you cry
- [ ] Colored output
- [ ] Activity statistics and graphs
- [ ] Multiple user comparison
- [ ] Star gazers tracking
- [ ] Contribution streak counter
- [ ] Integration with terminal notifications
- [ ] Web UI (just kidding... unless? 👀)



## 📞 Support & Contact

Having issues? Questions? Just want to chat about code?

- 🐛 [Open an issue](https://github.com/yourusername/github-activity/issues)
- 💬 [Start a discussion](https://github.com/yourusername/github-activity/discussions)
- 📧 Email: abydow@hotmail.com
- Linkedin: www.linkedin.com/in/abydow

## ⚠️ Disclaimer

This tool is for educational purposes .

## 🚀 Try It Now!


```bash
git clone https://github.com/yourusername/github-activity.git
cd github-activity
python github-activity.py torvalds
```

---

<div align="center">

**Made with ❤️, ☕, and probably too much caffeine**

If this project helped you, consider giving it a ⭐!

*"In code we trust, in bugs we debug."* 🐛

[⬆ Back to Top](#-github-user-activity-cli)

</div>
