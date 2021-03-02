from nameko.rpc import rpc
from dahuffman import HuffmanCodec
from dahuffman import load_shakespeare
from dahuffman import load_json_compact
from base64 import b64encode
from base64 import b64decode

class LearningChallengeService:
    name = "learning_challenge_service"

    def __init__(self):
        self.codec = load_shakespeare()

    def square_number_if_odd(self, num):
        if not type(num) is int:
            raise TypeError("Only integers are allowed")
        if (num % 2) == 0:
            return num
        else:
            return num * num


    @rpc
    def square_odd_numbers_in_list(self, numList):
        if not numList:
            raise ValueError("Empty list encountered")
        return list(map(self.square_number_if_odd, numList))

    @rpc
    def compress_string(self, plaintext):
        return b64encode(self.codec.encode(plaintext))

    @rpc
    def decode_string(self, encodedString):
        return self.codec.decode(b64decode(encodedString))

    @rpc
    def convert_string_list_to_encoded_dictionary(self, stringList):
        if not stringList:
            raise ValueError("Empty list encountered")
        return dict(zip(stringList, list(map(self.compress_string, stringList))))