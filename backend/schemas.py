from pydantic import BaseModel, ConfigDict
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    model_config = ConfigDict(
        from_attributes=True,  # replaces orm_mode
        json_schema_extra={    # replaces schema_extra
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }
    )


class Settings(BaseModel):
    authjwt_secret_key: str = (
        "b4bb9013c1c03b29b9311ec0df07f3b0d8fd13edd02d5c45b2fa7b86341fa405"
    )


class LoginModel(BaseModel):
    username: str
    password: str


class OrderModel(BaseModel):
    id: Optional[int] = None
    quantity: int
    order_status: Optional[str] = "PENDING"
    pizza_size: Optional[str] = "SMALL"
    user_id: Optional[int] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }
    )


class OrderStatusModel(BaseModel):
    order_status: Optional[str] = "PENDING"

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "order_status": "PENDING"
            }
        }
    )
