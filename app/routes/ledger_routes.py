from fastapi import APIRouter
from app.core.state import state
from app.services.ledger_service import LedgerService

router = APIRouter(prefix="/ledger", tags=["ledger"])


@router.get("")
def get_ledger():
    return {
        "node_id": state.node_info.node_id if state.node_info else None,
        "blocks": state.ledger,
        "pending_transactions": list(state.pending_transactions.values()),
        "confirmed_transactions": list(state.confirmed_transactions.values()),
    }


@router.post("/commit-pending")
def commit_pending():
    block = LedgerService.create_block_from_pending()
    if block is None:
        return {"message": "Nenhuma transação pendente"}

    LedgerService.commit_block(block)
    return {"message": "Bloco confirmado", "block": block}