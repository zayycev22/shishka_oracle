import unittest
from NeuralData.classifier import ShishkaClassifier


class TestRequalification(unittest.TestCase):
    def test_eq(self):
        first = "Запрос"
        second = "Запрос"
        assert ShishkaClassifier.get_requalification_type(first, second) == 0

    def test_upgrade(self):
        first = "Запрос"
        second = "Инцидент"
        assert ShishkaClassifier.get_requalification_type(first, second) == 1

    def test_downgrade(self):
        first = "Инцидент"
        second = "Запрос"
        assert ShishkaClassifier.get_requalification_type(first, second) == 2
