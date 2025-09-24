import re
from typing import Optional, Dict, List

class ShipmentNumberIdentifier:

    def __init__(self):
        # Define validation patterns for different shipment number types
        self.patterns = {
            'AWB': {
                'description': 'Air Waybill Number',
                'patterns': [
                    r'^\d{3}-\d{8}$',   # Standard AWB format: 000-00000000
                    r'^\d{11}$',        # 11-digit AWB without dash
                    r'^\d{3}\s\d{8}$',  # AWB with space separator
                ],
                'validation': self.validate_awb
            },
            'Container': {
                'description': 'Container Number',
                'patterns': [
                    r'^[A-Z]{4}\d{7}$',   # Standard container format: ABCD1234567
                    r'^[A-Z]{3}U\d{7}$',  # Common container prefix
                ],
                'validation': self.validate_container
            },
            'MBL': {
                'description': 'Master Bill of Lading',
                'patterns': [
                    r'^[A-Z]{3,4}\d{6,8}$',  # Common MBL format
                    r'^\d{9,12}$',           # Numeric MBL
                    r'^[A-Z]{2,3}\d{7,9}$',  # Mixed MBL format
                ],
                'validation': self.validate_mbl
            },
            'HBL': {
                'description': 'House Bill of Lading',
                'patterns': [
                    r'^[A-Z]{2,3}\d{6,8}$',   # Common HBL format
                    r'^HBL\d{6,9}$',          # HBL prefix format
                    r'^[A-Z]{3}HBL\d{5,7}$',  # Combined format
                ],
                'validation': self.validate_hbl
            },
            'Booking': {
                'description': 'Booking Reference Number',
                'patterns': [
                    r'^[A-Z]{3}\d{6,8}$',  # Standard booking format
                    r'^BR\d{7,9}$',        # Booking reference prefix
                    r'^\d{8,10}$',         # Numeric booking
                ],
                'validation': self.validate_booking
            }
        }

    def clean_input(self, number: str) -> str:
        """Remove spaces, dashes and convert to uppercase"""
        return re.sub(r'[\s\-]', '', number).upper()

    def validate_awb(self, number: str) -> bool:
        """Validate AWB number using checksum"""
        clean_num = number.replace('-', '').replace(' ', '')

        if len(clean_num) != 11:
            return False

        # AWB validation digit calculation
        try:
            digits = [int(d) for d in clean_num]
            check_digit = digits[-1]
            calculated_check = sum(digits[i] * (7 - i) for i in range(10)) % 11
            return calculated_check == check_digit
        except:
            return False

    def validate_container(self, number: str) -> bool:
        """Validate container number using ISO 6346 standard"""
        if len(number) != 11:
            return False

        # Container number validation
        mapping = {
            'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
            'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
            'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
        }

        try:
            total = 0
            for i, char in enumerate(number[:10]):
                if char.isdigit():
                    value = int(char)
                else:
                    value = mapping.get(char, 0)

                total += value * (2 ** i)

            check_digit = total % 11
            if check_digit == 10:
                check_digit = 0

            return check_digit == int(number[-1])
        except:
            return False

    def validate_mbl(self, number: str) -> bool:
        """Basic MBL validation"""
        # MBL numbers are often carrier-specific, so we use basic pattern matching
        return len(number) >= 9 and len(number) <= 15

    def validate_hbl(self, number: str) -> bool:
        """Basic HBL validation"""
        return len(number) >= 8 and len(number) <= 14

    def validate_booking(self, number: str) -> bool:
        """Basic booking reference validation"""
        return len(number) >= 8 and len(number) <= 12

    def identify_shipment_number(self, number: str) -> Dict:
        """Identify the type of shipment number"""
        if not number or not isinstance(number, str):
            return {'type': 'Unknown', 'confidence': 0, 'message': 'Invalid input'}

        clean_number = self.clean_input(number)
        results = []

        for num_type, info in self.patterns.items():
            # Check pattern matching
            pattern_matched = any(re.match(pattern, clean_number) for pattern in info['patterns'])

            # Check validation if pattern matches
            validation_passed = False
            confidence = 0

            if pattern_matched:
                validation_passed = info['validation'](clean_number)
                confidence = 85 if validation_passed else 60
            else:
                # Even if pattern doesn't match perfectly, try validation
                validation_passed = info['validation'](clean_number)
                if validation_passed:
                    confidence = 70

            if pattern_matched or validation_passed:
                results.append({
                    'type': num_type,
                    'description': info['description'],
                    'confidence': confidence,
                    'pattern_matched': pattern_matched,
                    'validation_passed': validation_passed
                })

        # Sort by confidence score
        results.sort(key=lambda x: x['confidence'], reverse=True)

        if results and results[0]['confidence'] > 50:
            best_match = results[0]
            return {
                'type': best_match['type'],
                'description': best_match['description'],
                'confidence': best_match['confidence'],
                'input_number': number,
                'cleaned_number': clean_number,
                'message': f'Identified as {best_match["description"]} with {best_match["confidence"]}% confidence'
            }
        else:
            return {
                'type': 'Unknown',
                'description': 'Unknown shipment number',
                'confidence': 0,
                'input_number': number,
                'cleaned_number': clean_number,
                'message': 'Could not identify the shipment number type'
            }

    def batch_identify(self, numbers: List[str]) -> List[Dict]:
        """Identify multiple shipment numbers at once"""
        return [self.identify_shipment_number(num) for num in numbers]


# Example usage and test function
def main():
    identifier = ShipmentNumberIdentifier()

    # Test cases
    test_numbers = [
        "123-45678901",  # AWB
        "ABCD1234567",  # Container
        "MAEU123456789",  # MBL
        "HLC1234567",  # HBL
        "COSU123456",  # Booking
        "618-12345675",  # AWB with valid check digit
        "TGHU2345678",  # Container with valid check digit
        "123456789012",  # Unknown
    ]

    print("Shipment Number Identification Results:")
    print("=" * 60)

    for number in test_numbers:
        result = identifier.identify_shipment_number(number)
        print(f"Input: {number:20} -> {result['type']:10} "
              f"(Confidence: {result['confidence']}%) - {result['message']}")


# Additional utility functions
def validate_specific_type(number: str, expected_type: str) -> bool:
    """Validate if a number matches a specific shipment type"""
    identifier = ShipmentNumberIdentifier()
    result = identifier.identify_shipment_number(number)
    return result['type'] == expected_type and result['confidence'] > 70


def extract_shipment_numbers(text: str) -> List[Dict]:
    """Extract and identify shipment numbers from text"""
    identifier = ShipmentNumberIdentifier()

    # Pattern to find potential shipment numbers
    patterns = [
        r'\b[A-Z]{3,4}\d{6,9}\b',  # Alphanumeric patterns
        r'\b\d{3}[- ]?\d{8}\b',  # AWB-like patterns
        r'\b[A-Z]{4}\d{7}\b',  # Container-like patterns
    ]

    found_numbers = []
    for pattern in patterns:
        matches = re.findall(pattern, text.upper())
        for match in matches:
            result = identifier.identify_shipment_number(match)
            if result['confidence'] > 60:
                found_numbers.append({
                    'number': match,
                    'type': result['type'],
                    'confidence': result['confidence'],
                    'description': result['description']
                })

    return found_numbers


if __name__ == "__main__":
    main()

    # Example of extracting from text
    sample_text = """
    Please track these shipments: 
    AWB 123-45678901, Container MSCU1234567, 
    MBL MAEU123456789, and Booking COSU123456.
    """

    print("\nExtracted shipment numbers from text:")
    print("=" * 50)
    extracted = extract_shipment_numbers(sample_text)
    for item in extracted:
        print(f"Found: {item['number']} -> {item['type']} ({item['confidence']}%)")