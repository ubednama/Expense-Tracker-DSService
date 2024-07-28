from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_mistralai import ChatMistralAI
from typing import Optional

class Expense(BaseModel):
    """Information about a transaction made on any Card"""
    amount: Optional[str] = Field(title="expense", description="Expense amount made in transaction")
    merchant: Optional[str] = Field(title="merchant", description="Merchant name for transaction")
    currency: Optional[str] = Field(title="currency", description="Currency for transaction")

    def serialize(self):
        return {
            "amount": self.amount,
            "merchant": self.merchant,
            "currency": self.currency
        }