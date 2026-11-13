# Z.ai Model Status & Compatibility

## Test Results (Current API Key)

This file documents all Z.ai GLM models tested for use with Hermes Agent.

### Working Models ✅
| Model ID              | Status    | Use Case             | Notes |
|-----------------------|-----------|----------------------|-------|
| `glm-4.7-flash`       | ✅ 1000   | Free tier, fallback | Requires higher max_tokens (>10) for content |
| `glm-4.5-flash`       | ✅ 1000   | Free tier, fallback | Tested, working with proper tokens |
| `glm-4-flash`         | ✅ 1000   | Free tier, fallback | Free tier model |

### Premium Models (Blocked ⚠️)
| Model ID | Status      | Reason                      | Alternative |
|----------|-------------|----------------------------|-------------|
| `glm-4.5` | ❌ 1113     | No balance/package          | -           |
| `glm-4.6` | ❌ 1113     | No balance/package          | -           |
| `glm-4.7` | ❌ 1113     | No balance/package          | -           |
| `glm-5`   | ❌ 1113     | No balance/package          | -           |
| `glm-5.1` | ❌ 1113     | No balance/package          | -           |
| `glm-5.2` | ❌ 1113     | No balance/package          | -           |
| `glm-5.3` | ❌ 1113     | No balance/package          | -           |
| `glm-5.3-flash` | ❌ 1113 | No balance/package | - |
| `glm-5.3-flashx` | ❌ 1113 | No balance/package | - |
| `glm-5.3-flashx-legal` | ❌ 1113 | No balance/package | - |

### API Error Codes
- `1000`: Success (model available, but may need higher `max_tokens`)
- `1113`: Insufficient balance or no resource package. Requires GLM Coding Plan or account upgrade.

## Usage Guide

### Recommended Models
```bash
# Recommended working (free tier)
zai/glm-4.7-flash
zai/glm-4.5-flash

# For testing/compatibility
zai/glm-4-flash
```

### Free Tier Limitations
- Models marked "Free tier" require no subscription.
- Premium models (`glm-5.x`, `glm-4.x`) require a paid GLM Coding Plan.
- Free models may limit token output or context length.

### Account Setup
To enable premium models:
1. Go to [Z.ai Account](https://z.ai/manage-apikey/apikey-list)
2. Subscribe to GLM Coding Plan (~$18/month)
3. Add API key to `install_zai.py`

## Future Updates
This file is updated with each new test run. Check the GitHub repository for the latest model status.

