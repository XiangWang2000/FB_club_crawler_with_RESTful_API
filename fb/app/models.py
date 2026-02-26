from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional

ItemType = Literal["post", "comment"]

class FeedItem(BaseModel):
    type: ItemType                # "post" or "comment"
    content: str
    time: datetime
    author: str
    post_id: Optional[str] = None # comment 對應的主文 id