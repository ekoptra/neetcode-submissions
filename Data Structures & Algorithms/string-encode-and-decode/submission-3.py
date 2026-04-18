class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            encode_str += f"{len(s)}"+ "#" + s + "#"
        
        print(encode_str)
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_list = []
        number_of_str = None
        split_s = ""
        split_number = ""

        for char in s:
            if number_of_str is None:
                if char == "#":
                    number_of_str = int(split_number)
                    split_number = ""
                else:
                    split_number += char 
            else:
                if number_of_str == 0:
                    if char == "#":
                        number_of_str = None
                        decode_list.append(split_s)
                        split_s = ""
                else:
                    number_of_str -= 1
                    split_s += char
    
        return decode_list 

