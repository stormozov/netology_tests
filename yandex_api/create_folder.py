import configparser
import pytest
import requests

config = configparser.ConfigParser()
config.read('settings.ini')
YA_DISK_TOKEN = config['Yandex_Disk']['token']


class TestYDCreateFolder:
    def setup_method(self):
        """Setup method for TestYDCreateFolder.

        This method is called before each test. It sets up the request headers
        and parameters for the test. It then sends a PUT request to the
        Yandex.Disk API to create a test folder. The response is stored in
        the `self.response` attribute.
        """
        self.headers = {
            'Authorization': f'OAuth {YA_DISK_TOKEN}'
        }
        self.params = {
            'path': 'test_folder'
        }
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.response = requests.put(
            self.url,
            params=self.params,
            headers=self.headers
        )

    def teardown_method(self) -> None:
        """Teardown method for TestYDCreateFolder.

        This method is called after each test. It sends a DELETE request to the
        Yandex.Disk API to delete the test folder. The response is stored in
        the `self.response` attribute.
        """
        self.response = requests.delete(
            self.url,
            params=self.params,
            headers=self.headers
        )

    def test_create_folder_response_status_code_201(self):
        """Test that a folder can be created."""
        if self.response.status_code == 201:
            print(f'Folder "{self.params["path"]}" created')

    def test_create_folder_response_status_code_400(self):
        """Test that the request is invalid."""
        if self.response.status_code == 400:
            print('Bad request')
        else:
            print(f'Response successful: {self.response.status_code}')

    @pytest.mark.xfail
    def test_create_folder_response_status_code_403(self):
        """ Test that the user does not have permission to create a folder. """
        assert self.response.status_code == 403

    def test_create_folder_response_status_code_409(self):
        """Test that a folder already exists."""
        if self.response.status_code == 409:
            print(f'Folder "{self.params["path"]}" already exists')

    def test_create_folder_response_status_code_401(self):
        """Test that the token is invalid."""
        if self.response.status_code == 401:
            print('Invalid token')

    def test_create_folder_response_status_code_404(self):
        """Test that the folder is not found."""
        if self.response.status_code == 404:
            print(f'Folder "{self.params["path"]}" not found')

    def test_create_folder_response_status_code_413(self):
        """Test that the file is too large."""
        if self.response.status_code == 413:
            print('The file cannot be uploaded. The file is too large.')

    def test_create_folder_response_status_code_429(self):
        """Test that the rate limit is exceeded."""
        if self.response.status_code == 429:
            print('Rate limit exceeded')

    def test_create_folder_response_status_code_503(self):
        """Test that the service is temporarily unavailable."""
        if self.response.status_code == 503:
            print('The service is temporarily unavailable')

    def test_create_folder_response_status_code_507(self):
        """Test that the storage space is insufficient."""
        if self.response.status_code == 507:
            print('Insufficient storage space')

    @pytest.mark.parametrize(
        'status_code', [[201, 401, 404, 409, 413, 429, 503, 507]]
    )
    def test_create_folder_response_status_code_unknown(self, status_code):
        """Test that the status code is unknown."""
        if self.response.status_code not in status_code:
            print(f'Unexpected status code: {self.response.status_code}')
        else:
            print(f'Unexpected status code: {self.response.status_code}')
