from unittest import TestCase
from unittest.mock import patch

from accounting.main import add_new_doc, directories, documents


class TestAddElement(TestCase):
    """ Tests for `add_new_doc` function. """

    def tearDown(self):
        """ Removes the added document from the `documents` list. """
        documents.pop()

        # Remove the added document from the directories dict
        for directory_docs_list in directories.values():
            if '12345' in directory_docs_list:
                directory_docs_list.remove('12345')
                break

    @staticmethod
    def _mock_input():
        """ Mocks `input` function. """
        with patch(
            'builtins.input',
            side_effect=['12345', 'passport', 'Иван Иванов', '1']
        ):
            return add_new_doc()

    def test_add_new_doc_length(self):
        """ Checks that `add_new_doc` appends new doc to `documents` list. """
        self._mock_input()
        self.assertEqual(
            len(documents),
            4,
            msg='Wrong length of `documents` list.'
        )

    def test_add_new_doc_number(self):
        """ Checks that `add_new_doc` appends new doc to `documents` list. """
        self._mock_input()
        self.assertIn(
            '12345',
            documents[-1]['number'],
            msg='Wrong value of `documents` list.'
        )

    def test_add_new_doc_directory(self):
        """ Checks that `add_new_doc` appends new doc to `directories` dict. """
        self._mock_input()
        self.assertIn(
            '12345',
            directories['1'],
            msg='Wrong value of `directories` dict.'
        )

    def test_add_new_doc_return_value(self):
        """ Checks that `add_new_doc` returns new doc's shelf number. """
        shelf_number = self._mock_input()
        self.assertEqual(
            shelf_number,
            '1',
            msg='Wrong return value of `add_new_doc` function.'
        )
