# Installation Guide with Signup Bonus

## Quick Start

### Option 1: Free Models (No Signup)
```bash
git clone https://github.com/m4tinbeigi-official/hermes-zai-connector.git
cd hermes-zai-connector
python3 install_zai.py
```

### Option 2: Premium Models (Recommended)
1. **Unlock premium with affiliate signup:**
   👉 **Subscribe now: https://z.ai/subscribe?ic=YMB12FKU68**

2. **Add premium API key:**
   ```bash
   ZAI_API_KEYS='your_premium_key' python3 install_zai.py
   ```

## What You Get

| Feature          | Free Tier          | Premium (with affiliate link) |
|------------------|-------------------|-----------------------------|
| `glm-4.7-flash`  | ✅                | ✅                          |
| `glm-4.5-flash`  | ✅                | ✅                          |
| `glm-5.2`       | ❌                | ✅ (best quality)           |
| `glm-5.1`       | ❌                | ✅                          |
| Coding tools     | Limited           | Full (20+ tools)            |
| Support         | Community         | Priority support            |

## Post-Install

1. Restart 9Router:
   ```bash
   launchctl kickstart -k "gui/$(id -u)/ai.hermes.9router"
   ```

2. Use models in Hermes:
   - Free: `zai/glm-4.7-flash`
   - Premium: `zai/glm-5.2`

---

Support open-source development by using our affiliate links when possible! 🚀
