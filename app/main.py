from fastapi import FastAPI
from app.config import get_node_info
from app.core.state import state
from app.routes.wallet_routes import router as wallet_router
from app.routes.transaction_routes import router as transaction_router
from app.routes.ledger_routes import router as ledger_router
from app.routes.internal_routes import router as internal_router

app = FastAPI(title="Crypto Distribuída")

state.node_info = get_node_info()

app.include_router(wallet_router)
app.include_router(transaction_router)
app.include_router(ledger_router)
app.include_router(internal_router)


@app.get("/")
def root():
    return {
        "message": "Nó da criptomoeda distribuída ativo",
        "node_id": state.node_info.node_id,
        "is_leader": state.node_info.is_leader,
        "port": state.node_info.port,
    }