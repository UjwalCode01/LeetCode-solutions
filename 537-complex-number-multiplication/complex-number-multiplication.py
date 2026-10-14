class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Parse the first complex number
        real1, imag1 = num1[:-1].split('+')
        a, b = int(real1), int(imag1)
        
        # Parse the second complex number
        real2, imag2 = num2[:-1].split('+')
        c, d = int(real2), int(imag2)
        
        # Calculate real and imaginary parts of the product
        real_part = (a * c) - (b * d)
        imag_part = (a * d) + (b * c)
        
        # Return the result as a string
        return f"{real_part}+{imag_part}i"