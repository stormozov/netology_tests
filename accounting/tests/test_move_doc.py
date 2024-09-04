from unittest import TestCase
from unittest.mock import patch

from accounting.main import directories, move_doc_to_shelf


class TestMoveDoc(TestCase):
    """ Testing moving document to another shelf """
    DOC_NUMBER = '5455 028765'
    SHELF_NUMBER_FOR_MOVE = '3'

    @staticmethod
    def _check_document_on_shelf(doc_number, shelf_number):
        """ Check that the document exists on the shelf """
        return doc_number in directories.get(shelf_number, [])

    def _find_original_shelf(self):
        """ Find the original shelf of the document """
        for directory_number, directory_docs_list in directories.items():
            if self.DOC_NUMBER in directory_docs_list:
                return directory_number
        return None

    def _assert_document_exists_on_shelf(self, shelf_number):
        """ Assert that the document exists on the shelf """
        self.assertIn(
            self.DOC_NUMBER,
            directories[shelf_number],
            f'The document {self.DOC_NUMBER} is missing '
            f'from the shelf {shelf_number}'
        )

    def _assert_document_does_not_exist_on_shelf(self, shelf_number):
        """ Assert that the document does not exist on the shelf """
        self.assertNotIn(
            self.DOC_NUMBER,
            directories[shelf_number],
            f'The document {self.DOC_NUMBER} is present on '
            f'the shelf {shelf_number}'
        )

    @patch('builtins.input', side_effect=[DOC_NUMBER, SHELF_NUMBER_FOR_MOVE])
    def test_move_doc_to_shelf(self, mock_input):
        """ Testing moving document to another shelf """
        print(
            'Тест: перемещение документа c существующей полки на выбранную '
            'полку'
        )
        original_shelf_number = self._find_original_shelf()

        self._assert_document_exists_on_shelf(original_shelf_number)
        print(f'Шаг 1. Документ  на текущий момент находится на полке:'
              f' {original_shelf_number}')

        print('Шаг 2. Вызываем функцию перемещения документа')
        move_doc_to_shelf()

        print('Шаг 3. Проверяем, что документ был перемещен')
        self._assert_document_does_not_exist_on_shelf(original_shelf_number)
        self._assert_document_exists_on_shelf(self.SHELF_NUMBER_FOR_MOVE)
