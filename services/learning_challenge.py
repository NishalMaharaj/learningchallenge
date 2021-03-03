from nameko.rpc import rpc
from dahuffman import HuffmanCodec
from dahuffman import load_shakespeare
from dahuffman import load_json_compact
from base64 import b64encode
from base64 import b64decode
import logging

class LearningChallengeService:
    name = "learning_challenge_service"

    def __init__(self):
        self.codec = load_shakespeare()
        logging.getLogger('simpleExample')

    def square_number_if_odd(self, num):
        if not type(num) is int:
            raise TypeError("Only integers are allowed")
        if (num % 2) == 0:
            return num
        else:
            return num * num


    @rpc
    def square_odd_numbers_in_list(self, numList):
        logging.info("square_odd_numbers_in_list Input: " + str(numList))
        if not numList:
            raise ValueError("Empty list encountered")
        response = list(map(self.square_number_if_odd, numList))
        logging.info("square_odd_numbers_in_list Output: " + str(response))
        return response

    def compress_string(self, plaintext):
        return b64encode(self.codec.encode(plaintext)).decode("utf-8")

    @rpc
    def decode_string(self, encodedString):
        logging.info("decode_string Input: " + str(encodedString))
        response = self.codec.decode(b64decode(encodedString))
        logging.info("decode_string Output: " + str(response))
        return response

    @rpc
    def convert_string_list_to_encoded_dictionary(self, stringList):
        logging.info("convert_string_list_to_encoded_dictionary Input: " + str(stringList))
        if not stringList:
            raise ValueError("Empty list encountered")
        response = dict(zip(stringList, list(map(self.compress_string, stringList))))
        logging.info("convert_string_list_to_encoded_dictionary Output: " + str(response))
        return response