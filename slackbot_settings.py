
import os

API_TOKEN = os.environ.get("SLACK_SHOGI_API_TOKEN", "")
DEPLOY_HOSTS = [os.environ.get("SLACK_SHOGI_DEPLOY_HOSTS", "")]
WEBHOOK_URL = os.environ.get("SLACK_SHOGI_WEBHOOK_URL", "")
