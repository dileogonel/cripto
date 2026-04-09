import os
from app.models.node_info import NodeInfo


def get_node_info() -> NodeInfo:
    node_id = os.getenv("NODE_ID", "node-1")
    host = os.getenv("NODE_HOST", "127.0.0.1")
    port = int(os.getenv("NODE_PORT", "8001"))
    is_leader = os.getenv("IS_LEADER", "false").lower() == "true"

    return NodeInfo(
        node_id=node_id,
        host=host,
        port=port,
        is_leader=is_leader,
    )