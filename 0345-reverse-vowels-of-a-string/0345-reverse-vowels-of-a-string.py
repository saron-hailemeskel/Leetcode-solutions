class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        left = 0
        right = len(chars) - 1

        while left < right:

            # Move left until it finds a vowel
            while left < right and chars[left] not in vowels:
                left += 1

            # Move right until it finds a vowel
            while left < right and chars[right] not in vowels:
                right -= 1

            # Swap the vowels
            chars[left], chars[right] = chars[right], chars[left]

            # Move both pointers
            left += 1
            right -= 1

        return ''.join(chars)