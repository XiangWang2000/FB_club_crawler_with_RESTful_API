from fastapi import FastAPI, Query
from typing import List, Optional, Literal
from .models import FeedItem
from .data_provider import list_items

app = FastAPI(
    title="FB Group Crawler API (Mock)",
    version="0.1.0",
    description="RESTful API for posts and comments (mock data)."
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items", response_model=List[FeedItem])
def get_items(
    months: int = Query(3, ge=1, le=12, description="Fetch items from last N months"),
    type: Optional[Literal["post", "comment"]] = Query(None, description="Filter by type"),
    post_id: Optional[str] = Query(None, description="Filter by post id (for comments)")
):
    """
    回傳欄位符合題目要求：
    - type: post/comment
    - content
    - time
    - author
    """
    return list_items(months=months, item_type=type, post_id=post_id)

@app.get("/posts", response_model=List[FeedItem])
def get_posts(months: int = Query(3, ge=1, le=12)):
    return list_items(months=months, item_type="post")

@app.get("/posts/{post_id}/comments", response_model=List[FeedItem])
def get_comments(post_id: str, months: int = Query(3, ge=1, le=12)):
    return list_items(months=months, item_type="comment", post_id=post_id)