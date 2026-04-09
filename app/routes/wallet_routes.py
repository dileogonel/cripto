from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.wallet_service import WalletService

router = APIRouter(prefix="/wallets", tags=["wallets"])


class CreateWalletRequest(BaseModel):
    public_key: str
    custody_type: str
    owner_name: str | None = None


@router.post("")
def create_wallet(payload: CreateWalletRequest):
    try:
        wallet = WalletService.create_wallet(
            public_key=payload.public_key,
            custody_type=payload.custody_type,
            owner_name=payload.owner_name,
        )
        return wallet
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/{wallet_id}/balance")
def get_balance(wallet_id: str):
    try:
        balance = WalletService.get_balance(wallet_id)
        return {"wallet_id": wallet_id, "balance": balance}
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))