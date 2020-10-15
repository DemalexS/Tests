from app import check_document_existance
from app import get_doc_owner_name
from app import add_new_doc
from app import get_doc_shelf
from app import delete_doc
from mock import patch
from app import yandex_add_folder


class TestScretary:
    def setup(self):
        print("method setup")

    def teardown(self):
        print("method teardown")

    def test_check_document_existance(self):
        assert check_document_existance('11-2') == True

    value = '11-2'

    @patch('builtins.input', return_value=value)
    def test_get_doc_owner_name(self, mock_input):
        result = get_doc_owner_name()
        assert result == 'Геннадий Покемонов'

    #new_doc_value = ['22-33', 'passport', 'Vasya', 2]

    @patch('builtins.input', side_effect=['22-33', 'passport', 'Vasya', 2])
    def test_add_new_doc(self, mock_input):
        result = add_new_doc()
        assert result == 2

    @patch('builtins.input', return_value="10006")
    def test_get_doc_shelf(self, mock_input):
        result = get_doc_shelf()
        assert result == '2'

    @patch('builtins.input', return_value="10006")
    def test_delete_doc(self, mock_input):
        result = delete_doc()
        assert result == ("10006", True)

    ya_token = '' #введите токен яндекс

    def test_yandex_add_folder(self, token=ya_token):
        result = yandex_add_folder(token, '2')
        assert result.status_code == 201

    def test_faild_yandex_add_folder(self, token=ya_token):
        result = yandex_add_folder(token, '2')
        assert result.status_code == 409

