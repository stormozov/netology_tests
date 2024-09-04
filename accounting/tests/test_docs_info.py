from unittest import TestCase
from unittest.mock import patch
from accounting.main import check_document_existence, get_doc_owner_name


class TestGetDocsInfo(TestCase):
    def test_doc_existence(self):
        """ Checks that `check_document_existence` returns True

        Checks that `check_document_existence` returns True
        if document exists and False if document does not exist.
        """
        doc_numbers = ['2207 876234', '11-2', '10006', '5455 028765']
        expected_results = [True, True, True, False]

        for doc_number, expected in zip(doc_numbers, expected_results):
            with self.subTest(doc_number=doc_number):
                result: bool = check_document_existence(doc_number)
                self.assertEqual(
                    expected,
                    result,
                    msg=f'Expected "{expected}" but got "{result}"'
                )

    @patch('builtins.input', side_effect=['2207 876234', '11-2', '10006'])
    def test_doc_owner_name_found(self, mock_input):
        """ Checks that `get_doc_owner_name` returns correct owner name

        Checks that `get_doc_owner_name` returns correct owner name
        if document exists and None if document does not exist.
        """
        expected_results = [
            'Василий Гупкин',
            'Геннадий Покемонов',
            'Аристарх Павлов'
        ]
        for expected in expected_results:
            self.assertEqual(
                get_doc_owner_name(),
                expected,
                msg=f'Expected "{expected}" but got "{get_doc_owner_name()}"'
            )
