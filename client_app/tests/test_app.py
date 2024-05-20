"""
Integration tests for the Streamlit application.
"""
import unittest
from unittest.mock import patch, mock_open, MagicMock
from streamlit.testing.v1 import AppTest

class TestStreamlitApp(unittest.TestCase):
    """
    Test the functionality of the Streamlit client application.
    """
    def setUp(self):
        """
        Initialize AppTest and run the Streamlit app.
        """
        self.at = AppTest.from_file("../app.py", default_timeout=5)
        self.at.run()

    def print_markdown_elements(self):
        """
        Helper function to print markdown elements for debugging.
        """
        print("Markdown Elements:")
        for elem in self.at.markdown:
            print(elem.value)

    @patch('client_app.networking.send_dictionary')
    @patch('streamlit.success')
    def test_send_dictionary(self, mock_success, mock_send_dictionary):
        """
        Test sending a dictionary via the Streamlit app.
        """
        self.at.selectbox("action_select").select("Send Dictionary").run()
        self.at.text_input("dict_key").set_value("test").run()
        self.at.number_input("dict_value").set_value(42).run()
        self.at.selectbox("dict_serialize_format").select("json").run()
        self.at.button("send_dict_btn").click().run()

        mock_send_dictionary.assert_called_once_with({'key': 'test', 'value': 42}, 'json')
        mock_success.assert_called_once_with("Dictionary sent successfully!")

    @patch('client_app.networking.send_text_file')
    @patch('builtins.open', new_callable=mock_open, read_data=b'test file data')
    @patch('streamlit.success')
    def test_send_text_file(self, mock_success, mock_file, mock_send_text_file):
        """
        Test sending a text file via the Streamlit app.
        """
        with patch('streamlit.file_uploader') as mock_file_uploader:
            mock_file_uploader.return_value = MagicMock(name="example.txt")

            self.at.selectbox("action_select").select("Send Text File").run()
            mock_file_uploader.return_value = MagicMock()
            mock_file_uploader().name = "example.txt"
            mock_file_uploader().getvalue.return_value = b"example file content"

            self.at.checkbox("encrypt_checkbox").check().run()
            self.at.button("send_file_btn").click().run()

            mock_send_text_file.assert_called_once_with('temp_example.txt', True)

            mock_success.assert_called_once_with("Text file sent successfully!")

if __name__ == '__main__':
    unittest.main()
