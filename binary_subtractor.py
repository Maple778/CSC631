class BinarySubtractor:
    def __init__(self, bit_width=4):
        self.bit_width = bit_width
        self.max_value = (1 << bit_width) - 1  # Maximum value for given bit width

    # Convert decimal to binary with step-by-step process
    def decimal_to_binary(self, num):
        if num == 0:
            return '0' * self.bit_width

        binary = ''
        original_num = num
        steps = []

        while num > 0:
            remainder = num & 1  # Use bitwise AND to get remainder
            quotient = num >> 1  # Use right shift for division by 2
            steps.append(f"{num} ÷ 2 = {quotient} remainder {remainder}")
            binary = str(remainder) + binary
            num = quotient

        # Pad with leading zeros to match bit width
        binary = binary.zfill(self.bit_width)

        print(f"Converting {original_num} to binary:")
        for step in steps:
            print(f"  {step}")
        print(f"  Reading remainders bottom-up: {binary}")
        print()

        return binary

    # Implement NOT gate
    def binary_not(self, binary_str):
        result = ''
        for bit in binary_str:
            if bit == '0':
                result += '1'
            else:
                result += '0'
        return result

    # XOR three bits together
    def xor_three_bits(self, a, b, c):
        # a + b + c
        temp = '1' if a != b else '0'
        return '1' if temp != c else '0'

    # Add two binary numbers using logic gates
    def binary_add(self, a, b):
        result = ''
        carry = '0'

        print(f"Adding {a} + {b}:")

        # Process from right to left
        for i in range(len(a) - 1, -1, -1):
            # XOR for sum without carry
            sum_bit = self.xor_three_bits(a[i], b[i], carry)

            # Calculate new carry using AND gates
            carry_ab = '1' if (a[i] == '1' and b[i] == '1') else '0'
            carry_ac = '1' if (a[i] == '1' and carry == '1') else '0'
            carry_bc = '1' if (b[i] == '1' and carry == '1') else '0'

            # New carry is OR of all carry conditions
            new_carry = '1' if (carry_ab == '1' or carry_ac == '1' or carry_bc == '1') else '0'

            result = sum_bit + result
            print(f"  Position {len(a) - 1 - i}: {a[i]} + {b[i]} + {carry} = {sum_bit}, carry = {new_carry}")
            carry = new_carry

        # Ignore final carry for fixed bit width
        if carry == '1':
            print(f"  Final carry {carry} ignored (overflow)")

        print(f"  Result: {result}")
        print()
        return result

    # Convert to negative number
    def conv_neg(self, binary_str):

        print(f"Finding two's complement of {binary_str}:")

        # Step 1: Flip all bits (NOT operation)
        flipped_bits = self.binary_not(binary_str)
        print(f"  Flip all bits: {flipped_bits}")

        # Step 2: Add 1
        one = '0' * (self.bit_width - 1) + '1'
        negative_b = self.binary_add(flipped_bits, one)

        print(f"  Two's complement: {negative_b}")
        print()
        return negative_b

    # Subtract B from A using two's complement method
    def binary_subtract(self, a_dec, b_dec):
        print(f"Computing {a_dec} - {b_dec} using binary logic")
        print()

        # Convert to binary
        a_bin = self.decimal_to_binary(a_dec)
        b_bin = self.decimal_to_binary(b_dec)

        print(f"A = {a_dec} in binary: {a_bin}")
        print(f"B = {b_dec} in binary: {b_bin}")
        print()

        # Get neg_b
        neg_b = self.conv_neg(b_bin)

        # A + (-B)
        print(f"Computing A + (-B):")
        result_bin = self.binary_add(a_bin, neg_b)

        # Convert result to decimal
        result_dec = self.binary_to_decimal(result_bin)

        print(f"Final Result:")
        print(f"  Binary: {result_bin}")
        print(f"  Decimal: {result_dec}")
        print()

    # Convert binary string to decimal
    def binary_to_decimal(self, binary_str):
        decimal = 0
        for i, bit in enumerate(reversed(binary_str)):
            if bit == '1':
                decimal += (1 << i)  # 2^i
        return decimal

def main():
    # Task 1: Binary Representation
    print("Task 1: Binary Representation")
    # Use a 4-bit subtractor for the small numbers
    subtractor_4bit = BinarySubtractor(4)
    subtractor_4bit.decimal_to_binary(5)
    subtractor_4bit.decimal_to_binary(3)
    subtractor_4bit.decimal_to_binary(2)

    # Task 2: Subtraction with Two’s Complement
    print("Task 2: Subtraction with Two’s Complement")
    # Example: 0101 - 0011 (5 - 3)
    print("Computing 0101 - 0011 (5 - 3):")
    subtractor_4bit.binary_subtract(5, 3)

    # Requirement Test: A = 60, B = 40
    print("Requirement Test: A = 60, B = 40")
    # Initialize 8-bit subtractor for larger numbers
    subtractor_8bit = BinarySubtractor(8)
    subtractor_8bit.binary_subtract(60, 40)

# add comment by ying

if __name__ == "__main__":
    main()
