class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        number_of_bytes = 0

        # Masks for checking the leading bits
        mask1 = 1 << 7  # 10000000
        mask2 = 1 << 6  # 01000000

        for num in data:
            # Mask to isolate the least significant 8 bits
            num = num & 255

            if number_of_bytes == 0:
                # Determine how many bytes the current UTF-8 character consists of
                mask = 1 << 7
                while mask & num:
                    number_of_bytes += 1
                    mask = mask >> 1

                # 1-byte character
                if number_of_bytes == 0:
                    continue

                # Invalid character length (UTF-8 bytes are 1 to 4)
                if number_of_bytes == 1 or number_of_bytes > 4:
                    return False
            else:
                # Must start with '10'
                if not (num & mask1 and not (num & mask2)):
                    return False

            # Decrement expected remaining continuation bytes
            number_of_bytes -= 1

        return number_of_bytes == 0