from nameko.testing.services import worker_factory
from services.learning_challenge import LearningChallengeService
import pytest
import base64

def test_is_integer_value():
    service = worker_factory(LearningChallengeService)
    with pytest.raises(TypeError):
        service.square_number_if_odd('Hello')

def test_is_blank_integer_list():
    service = worker_factory(LearningChallengeService)
    with pytest.raises(ValueError):
        service.square_odd_numbers_in_list([])

def test_odd_number():
    service = worker_factory(LearningChallengeService)
    assert(service.square_number_if_odd(3) == 9)

def test_even_number():
    service = worker_factory(LearningChallengeService)
    assert(service.square_number_if_odd(2) == 2)

def test_ordered_list():
    service = worker_factory(LearningChallengeService)
    assert(service.square_odd_numbers_in_list(
        [1, 2, 3, 4, 5]) == [1, 2, 9, 4, 25])

def test_is_blank_string_list():
    service = worker_factory(LearningChallengeService)
    with pytest.raises(ValueError):
        service.convert_string_list_to_encoded_dictionary([])

def test_compress_string():
    service = worker_factory(LearningChallengeService)
    assert(len(base64.b64decode(service.compress_string('What the hell!1'))) == 10)

def test_decode_string():
    service = worker_factory(LearningChallengeService)
    assert(service.decode_string(service.compress_string(
        'What the hell!1')) == 'What the hell!1')

def test_compressed_dictionary_size():
    service = worker_factory(LearningChallengeService)
    assert(len(service.convert_string_list_to_encoded_dictionary(
        ['THIS', 'THIS', 'A', 'TEST'])) == 3)

