#!/usr/bin/env python3
"""
Deserialization Module.

This module provides a function for deserializing data from binary, JSON, and XML.
"""

import pickle
import json
import xml.etree.ElementTree as ET

def deserialize(data, serialization_format):
    """
    Deserializes the given data based on the specified format.

    Args:
        data (bytes): The serialized data to deserialize.
        serialization_format (str): The format of the serialized data ('binary', 'json', 'xml').

    Returns:
        dict: The deserialized dictionary.
    """
    if serialization_format == "binary":
        return pickle.loads(data)
    elif serialization_format == "json":
        return json.loads(data.decode('utf-8'))
    elif serialization_format == "xml":
        root = ET.fromstring(data)
        return {child.tag: child.text for child in root}
    else:
        raise ValueError("Invalid serialization format")
