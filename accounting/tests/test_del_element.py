from unittest import TestCase
from unittest.mock import patch

from accounting.main import delete_doc


class TestDelElement(TestCase):
    def test_remove_doc_from_shelf(self):
        """ Test remove doc from shelf """
        @patch('accounting.main.input', return_value='2207 876234')
        @patch(
            'accounting.main.directories',
            {
                '1': ['2207 876234', '11-2'],
                '2': ['10006']
            }
        )
        @patch(
            'accounting.main.documents',
            [
                {
                    'type': 'passport', 'number': '2207 876234',
                    'name': 'Василий Гупкин'
                },
                {
                    'type': 'invoice', 'number': '11-2',
                    'name': 'Геннадий Покемонов'
                }
            ]
        )
        def test_delete_doc(mock_input, mock_directories, mock_documents):
            """ Test remove doc from shelf """
            result: tuple = delete_doc()

            self.assertEqual(
                result,
                (mock_input, True),
                'The function should return a tuple with two elements: '
                'the first element is the document number, the second is True'
            )
            self.assertNotIn(
                mock_input,
                mock_directories['1'],
                'The function should remove the document from '
                'the list of shelves'
            )
            self.assertEqual(
                len(mock_documents),
                1,
                'The function should remove the document '
                'from the list of documents'
            )
