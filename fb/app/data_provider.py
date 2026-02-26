import json
from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import List, Optional
from .models import FeedItem

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "mock_data.json"
UTC = timezone.utc


def load_data() -> List[FeedItem]:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)

    items = []
    for x in raw:
        items.append(
            FeedItem(
                type=x["type"],
                content=x["content"],
                time=datetime.fromisoformat(x["time"]).replace(tzinfo=UTC),
                author=x["author"],
                post_id=x.get("post_id"),
            )
        )
    return items


def list_items(months=3, item_type=None, post_id=None):
    items = load_data()

    cutoff = datetime.now(tz=UTC) - timedelta(days=30 * months)
    items = [x for x in items if x.time >= cutoff]

    if item_type:
        items = [x for x in items if x.type == item_type]

    if post_id:
        items = [x for x in items if x.post_id == post_id]

    return sorted(items, key=lambda x: x.time, reverse=True)