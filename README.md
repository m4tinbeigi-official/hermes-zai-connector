# Hermes Agent + Z.ai

Add Z.ai's OpenAI-compatible GLM endpoint to local 9Router and use it from Hermes Agent.

## Requirements

- macOS or Linux
- Python 3.10+
- 9Router installed and running once
- Z.ai API key(s)

## Install

Clone repository, then run:

```bash
python3 install_zai.py
```

Installer prompts for one key. For multiple keys, pass keys through environment, never commit them:

```bash
ZAI_API_KEYS='key_one,key_two,key_three' python3 install_zai.py
```

Or pass them as arguments. Shell history may retain arguments, so environment is safer:

```bash
python3 install_zai.py key_one key_two
```

Keys stay in local 9Router SQLite database at `~/.9router/db/data.sqlite`. This repository contains no keys.

Restart 9Router after installation:

```bash
launchctl kickstart -k "gui/$(id -u)/ai.hermes.9router"  # macOS
```

Use model in Hermes:

```text
zai/glm-4.7-flash
```

Base URL:

```text
https://api.z.ai/api/coding/paas/v4
```

## Multiple accounts and automatic switching

Create only accounts allowed by Z.ai's current Terms of Service and plan rules. Do not create accounts to evade limits, identity checks, bans, or billing controls.

You may enter multiple API keys from legitimately owned/authorized accounts. Installer creates one active 9Router connection per key. 9Router can rotate/fallback between connections when an upstream key is unavailable, rate-limited, or quota-blocked. Keep keys on separate authorized accounts only when Z.ai permits that arrangement.

No fixed universal limit exists in this project. Maximum usable keys depends on Z.ai's account, plan, API-key, rate, and abuse policies. Check Z.ai dashboard and Terms before adding more.

## Model Status

### ✅ Working Models (Free Tier)
- `zai/glm-4.7-flash` — recommended fallback, requires high max_tokens
- `zai/glm-4.5-flash` — free tier, tested working
- `zai/glm-4-flash` — free tier, basic compatibility

### ⚠️ Premium Models (Requires Coding Plan)
- `zai/glm-5.2` — latest, best quality, needs GLM Coding Plan
- `zai/glm-5.1`, `zai/glm-5-turbo`, `zai/glm-5` — higher tier models

Upgrade to premium:
- Visit [Z.ai Management Console](https://z.ai/manage-apikey/apikey-list)
- Subscribe to GLM Coding Plan (~$18/month)
- Enter premium API key to enable `glm-5.2` and other models

### Error Codes
- `1000`: Success (model available, may need proper `max_tokens`)
- `1113`: Insufficient balance (requires paid subscription)

For full model details, see [MODEL_STATUS.md](MODEL_STATUS.md).

## Usage

```bash
# Use working free models
zai/glm-4.7-flash
zai/glm-4.5-flash

# Premium models after upgrade
zai/glm-5.2  # highest quality, requires plan
```

## Security

- Never commit API keys.
- Never paste keys into GitHub Issues, README, logs, or screenshots.
- Revoke exposed keys in Z.ai dashboard.
- Use `ZAI_API_KEYS` from a protected shell or secret manager.
- This installer writes keys to local 9Router storage because 9Router needs them to route requests.

## License

MIT
## Extended Resources
- [Installation Guide with Affiliate Signup](INSTALL_GUIDE.md) — Quick start with free/premium options  
- [Full Model Status](MODEL_STATUS.md) — All tested models and compatibility  
- [Affiliate Disclosure](AFFILIATE_DISCLOSURE.md) — How this project supports development
