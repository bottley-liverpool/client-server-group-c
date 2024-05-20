"""
Deserialization unit tests module
"""
import unittest
import pickle
import json
import xml.etree.ElementTree as ET
from server_app.deserialization import deserialize

class TestDeserialization(unittest.TestCase):
    """
    Test the deserialize function
    """
    def setUp(self):
        """
        Set up test data for deserialization
        """
        self.test_dict = {'key': 'test', 'value': 30}
        self.binary_data = pickle.dumps(self.test_dict)
        self.json_data = json.dumps(self.test_dict).encode('utf-8')

        # Create an XML representation with string values
        root = ET.Element('root')
        for key, value in self.test_dict.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Ensure the text is a string
        self.xml_data = ET.tostring(root)

    def test_deserialize_binary(self):
        """
        Test deserialization of binary data
        """
        result = deserialize(self.binary_data, 'binary')
        self.assertEqual(result, self.test_dict)

    def test_deserialize_json(self):
        """
        Test deserialization of JSON data
        """
        result = deserialize(self.json_data, 'json')
        self.assertEqual(result, self.test_dict)

    def test_deserialize_xml(self):
        """
        Test deserialization of XML data
        """
        result = deserialize(self.xml_data, 'xml')
        self.assertEqual(result, {child.tag: child.text for child in ET.fromstring(self.xml_data)})

    def test_invalid_format(self):
        """
        Test deserialization with an invalid format
        """
        with self.assertRaises(ValueError):
            deserialize(self.binary_data, 'invalid_format')

if __name__ == "__main__":
    unittest.main()
