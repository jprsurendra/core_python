import re

def identify_tracking_number(tracking_no: str) -> str:
    tracking_no = tracking_no.strip().upper()
    '''
    1. Check AWB Number (Air Waybill)
        Format: 3-digit airline prefix + 8-digit serial (total 11 digits).    
        Example: 07112345678, 23598765432.    
        Sometimes written as 071-12345678.
    '''
    if re.match(r"^\d{3}[- ]?\d{8}$", tracking_no):
        return "AWB Number"

    # 2. Check Container Number
    '''
    '''
    if re.match(r"^[A-Z]{4}\d{7}$", tracking_no):
        return "Container Number"

    # 3. Check MBL (heuristic: alphanumeric 8–12 chars, not AWB/Container)
    if re.match(r"^[A-Z0-9]{8,12}$", tracking_no):
        return "MBL Number"

    # 4. Otherwise assume Line Booking Number
    return "Line Booking Number"


# ---------------- Demo ----------------
test_numbers = [
    "07112345678",   # AWB
    "071-12345678",  # AWB
    "MSCU1234567",   # Container
    "OOLU123456789", # MBL
    "BK123456",      # Booking
    "12345678"       # Booking
]

for t in test_numbers:
    print(f"{t} -> {identify_tracking_number(t)}")
