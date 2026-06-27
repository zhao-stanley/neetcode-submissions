class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        if not strs:
            return ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i=0
        while i < len(s):
            length = ""
            j = i
            while s[j] != "#":
                length += s[j]
                j += 1
            eow = j + 1 + int(length)
            decoded_chunk = s[j + 1:eow]
            decoded.append(decoded_chunk)
            i = eow

        return decoded


