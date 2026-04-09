from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Transaction(BaseModel):
    transaction_id: str
    sender_wallet_id: str
    receiver_wallet_id: str
    amount: float
    signature: str
    timestamp: datetime
    status: str = "pending"
    block_id: Optional[str] = None