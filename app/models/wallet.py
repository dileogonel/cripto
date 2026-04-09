from pydantic import BaseModel
from typing import Optional


class Wallet(BaseModel):
    wallet_id: str
    public_key: str
    custody_type: str  # "self" ou "exchange"
    owner_name: Optional[str] = None