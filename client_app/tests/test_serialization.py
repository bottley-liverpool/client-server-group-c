"""
Serialization unit tests module
"""
import unittest
import pickle
import json
import xml.etree.ElementTree as ET
from client_app.serialization import serialize

class TestSerialization(unittest.TestCase):
    """
    Test the serialization functions
    """
    def setUp(self):
        """
        Set up test data for serialization
        """
        self.test_dict = {'key': 'test', 'value': 30}
        self.binary_data = pickle.dumps(self.test_dict)
        self.json_data = json.dumps(self.test_dict).encode('utf-8')

        root = ET.Element('root')
        for key, value in self.test_dict.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        self.xml_data = ET.tostring(root)

    def test_serialize_binary(self):
        """
        Test serialization to binary format
        """
        result = serialize(self.test_dict, 'binary')
        self.assertEqual(result, self.binary_data)

    def test_serialize_json(self):
        """
        Test serialization to JSON format
        """
        result = serialize(self.test_dict, 'json')
        self.assertEqual(result, self.json_data)

    def test_serialize_xml(self):
        """
        Test serialization to XML format
        """
        result = serialize(self.test_dict, 'xml')
        self.assertEqual(result, self.xml_data)

    def test_invalid_format(self):
        """
        Test serialization with an invalid format
        """
        with self.assertRaises(ValueError):
            serialize(self.test_dict, 'invalid_format')

if __name__ == "__main__":
    unittest.main()
