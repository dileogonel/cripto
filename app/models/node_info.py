from pydantic import BaseModel


class NodeInfo(BaseModel):
    node_id: str
    host: str
    port: int
    is_leader: bool = False