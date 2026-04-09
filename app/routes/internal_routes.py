from fastapi import APIRouter
from app.core.state import state

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/health")
def health():
    return {
        "status": "ok",
        "node_id": state.node_info.node_id if state.node_info else None,
        "is_leader": state.node_info.is_leader if state.node_info else False,
    }