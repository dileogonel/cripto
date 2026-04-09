from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.models.transaction import Transaction


class Block(BaseModel):
    block_id: str
    previous_hash: str
    transactions: List[Transaction]
    timestamp: datetime
    proposer_node_id: str
    block_hash: str