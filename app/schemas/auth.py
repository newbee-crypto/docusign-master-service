from pydantic import BaseModel, Field 

class ValidateCredentials(BaseModel):
    client_id: str = Field(..., description="The client ID for authentication")
    user_id:str = Field(..., description="The user ID for authentication")
    private_key_pem :str = Field(..., description="The private key in PEM format for authentication")
    account_id:str | None =  None

class ValidateCredentialsResponse(BaseModel):
    client_id: str
    user_id: str
    account_id: str | None = None
