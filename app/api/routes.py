from fastapi import APIRouter
import asyncio
from schemas.auth import ValidateCredentials, ValidateCredentialsResponse
router = APIRouter(prefix="/api/v1")
from fastapi import Depends




@router.get("/health",status_code=200)
def health_check():
    return {"status":" OK "}

@router.post("/validate-credentials",response_model = ValidateCredentialsResponse)
def validate_credentials(validate : ValidateCredentials):
    return {"client_id": validate.client_id, "user_id": validate.user_id, "account_id": validate.account_id}


