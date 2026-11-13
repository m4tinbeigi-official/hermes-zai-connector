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

## Models

- `glm-4.7-flash`: default
- `glm-4.5-flash`: fallback
- `glm-5.2`: available when account has required plan or balance

Model availability and quota come from Z.ai. A valid key without an eligible resource package may return error `1113`.

## Security

- Never commit API keys.
- Never paste keys into GitHub Issues, README, logs, or screenshots.
- Revoke exposed keys in Z.ai dashboard.
- Use `ZAI_API_KEYS` from a protected shell or secret manager.
- This installer writes keys to local 9Router storage because 9Router needs them to route requests.

## License

MIT
