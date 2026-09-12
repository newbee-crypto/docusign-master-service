from fastapi import APIRouter
router = APIRouter()



@router.get("/api/v1/health",status_code=200)
def health_check():
    return {"status": "ok"}