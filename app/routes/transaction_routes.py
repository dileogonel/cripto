from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["transactions"])


class CreateTransactionRequest(BaseModel):
    sender_wallet_id: str
    receiver_wallet_id: str
    amount: float
    signature: str


@router.post("")
def create_transaction(payload: CreateTransactionRequest):
    try:
        tx = TransactionService.create_transaction(
            sender_wallet_id=payload.sender_wallet_id,
            receiver_wallet_id=payload.receiver_wallet_id,
            amount=payload.amount,
            signature=payload.signature,
        )
        return tx
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))