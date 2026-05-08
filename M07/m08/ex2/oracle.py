import sys
import logging

# -- Dependency check ---------------------------------------------------------
try:
    from dotenv import load_dotenv
except ImportError:
    print("[ERROR] python-dotenv is not installed.")
    print("  pip:    pip install python-dotenv")
    print("  poetry: poetry add python-dotenv")
    sys.exit(1)

import os

# -- Load .env (only in development; production uses real env vars) -----------
load_dotenv()

# -- Required variables -------------------------------------------------------
_REQUIRED = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]

_missing = [k for k in _REQUIRED if not os.getenv(k)]
if _missing:
    print("[ERROR] Missing required environment variables:")
    for k in _missing:
        print(f"  - {k}")
    print("\nCopy .env.example to .env and fill in your values.")
    sys.exit(1)

MATRIX_MODE    = os.getenv("MATRIX_MODE")
DATABASE_URL   = os.getenv("DATABASE_URL")
API_KEY        = os.getenv("API_KEY")
LOG_LEVEL      = os.getenv("LOG_LEVEL", "INFO").upper()
ZION_ENDPOINT  = os.getenv("ZION_ENDPOINT")

# -- Logging ------------------------------------------------------------------
logging.basicConfig(
    stream=sys.stdout,
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="[%(levelname)s] %(message)s",
)
log = logging.getLogger("oracle")

# -- Mode-specific behaviour --------------------------------------------------
IS_DEV = MATRIX_MODE.lower() == "development"

def _mask(secret: str) -> str:
    """Show only first 4 chars of a secret."""
    return secret[:4] + "*" * (len(secret) - 4) if len(secret) > 4 else "****"

# -- Boot sequence ------------------------------------------------------------
print("=" * 52)
print("  THE ORACLE — Secure Configuration System")
print("=" * 52)
print(f"\nMode         : {MATRIX_MODE.upper()}")
print(f"Log level    : {LOG_LEVEL}")
print(f"Database     : {DATABASE_URL if IS_DEV else '[REDACTED in production]'}")
print(f"API key      : {_mask(API_KEY)}")
print(f"Zion endpoint: {ZION_ENDPOINT}")
print()

if IS_DEV:
    log.debug("Debug logging active — verbose output enabled")
    log.info("Development mode: .env file loaded via python-dotenv")
    log.warning("Do NOT use development credentials in production")
else:
    log.info("Production mode: shell/host environment variables take priority over .env")
    log.info("Any variable already set in the environment is NOT overridden by .env")

# -- Simulated pipeline -------------------------------------------------------
print("\n-- Connecting to systems --")

log.info(f"Connecting to database: {DATABASE_URL if IS_DEV else '[hidden]'}")
print(f"  [OK] Database connection established")

log.info(f"Authenticating with API key {_mask(API_KEY)}")
print(f"  [OK] API authentication successful")

log.info(f"Reaching Zion endpoint: {ZION_ENDPOINT}")
print(f"  [OK] Zion endpoint reachable")

print("\n-- Oracle is ready --")
if IS_DEV:
    print("  Tip: set MATRIX_MODE=production (and real env vars) to see production behaviour.")
else:
    print("  Running in production — all secrets sourced from the host environment.")
