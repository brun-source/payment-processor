import logging
import re
from decimal import Decimal

def validate_email(email: str) -> bool:
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_pattern, email))

def validate_phone_number(phone_number: str) -> bool:
    phone_pattern = r"^\(\d{3}\)\s?\d{3}-\d{4}$"
    return bool(re.match(phone_pattern, phone_number))

def validate_credit_card_number(card_number: str) -> bool:
    card_number = card_number.strip()
    if len(card_number) < 13 or len(card_number) > 16:
        return False
    return True

def calculate_total(items: list) -> Decimal:
    return Decimal(sum(item['price'] * item['quantity'] for item in items))

def configure_logging(log_level: str = 'INFO'):
    numeric_log_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_log_level, int):
        raise ValueError("Invalid log level")
    logging.basicConfig(level=numeric_log_level)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)

def process_payment(card_number: str, cvv: str, expiration_date: str, amount: Decimal, items: list) -> str:
    if not validate_credit_card_number(card_number):
        return "Invalid card number"
    if not validate_cvv(cvv):
        return "Invalid CVV"
    if not validate_expiration_date(expiration_date):
        return "Invalid expiration date"
    if amount <= 0:
        return "Invalid amount"
    total = calculate_total(items)
    if amount < total:
        return "Insufficient funds"
    logger = get_logger('payment_processor')
    logger.info(f"Processing payment: ${amount} for items: {[item['name'] for item in items]}")
    return "Payment processed successfully"

def validate_cvv(cvv: str) -> bool:
    cvv_pattern = r"^\d{3,4}$"
    return bool(re.match(cvv_pattern, cvv))

def validate_expiration_date(expiration_date: str) -> bool:
    expiration_date_pattern = r"^\d{2}/\d{2}$"
    return bool(re.match(expiration_date_pattern, expiration_date))