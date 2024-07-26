from langchain_core.pydantic_v1 import BaseModel, Field
from datetime import datetime
from typing import Optional
from utils.messageUtil import MessageUtil

class Expense(BaseModel):
    amount: Optional[str] = Field(title="expense", description="Expense amount made in transaction")
    merchant: Optional[str] = Field(title="merchant", description="Merchant name for transaction")
    currency: Optional[str] = Field(title="currency", description="Currency for transaction")