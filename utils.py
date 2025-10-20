"""
utils.py — helper utilities

1. generate_account_id(prefix="ACC"):
   - Use uuid.uuid4().hex[:6] to generate a short unique ID.

2. current_timestamp():
   - Return timestamp as string, e.g. "2025-09-17 10:15:00".
"""

import uuid
from datetime import datetime

def generate_account_id(prefix="ACC"):
    return f"{prefix}-{uuid.uuid4().hex[:6]}"

def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# -*- coding: utf-8 -*-

