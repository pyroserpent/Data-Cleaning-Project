import pandas as pd
import re

def clean_phone_number(phone):
    """Cleans and formats phone numbers into (XXX) XXX XXXX format."""
    if pd.isna(phone) or str(phone).strip().lower() in ["n/a", "nan", "none", ""]:
        return None  # Handle NaN, "N/a", "None", empty strings
    
    phone_str = str(phone).strip()
    digits = re.sub(r'\D', '', phone_str)  # Remove non-numeric characters

    # Remove leading "1" for US numbers
    if len(digits) == 11 and digits.startswith('1'):
        digits = digits[1:]
    
    # Ensure it's a valid 10-digit number
    if len(digits) != 10:
        return None  
    
    # Format: (XXX) XXX XXXX
    return f"({digits[:3]}) {digits[3:6]} {digits[6:]}"

# Example usage:
if __name__ == "__main__":
    sample_numbers = ["123-456-7890", "1-800-555-0199", "876|678|3469", "N/a", "123/643/9775"]
    cleaned_numbers = [clean_phone_number(num) for num in sample_numbers]
    print(cleaned_numbers)
