from fastapi import APIRouter

router = APIRouter()

@router.post('/agent')
def agent_route():
    return None