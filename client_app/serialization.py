#!/usr/bin/env python3
"""
Serialization Module.

This module provides functions for serializing data into various formats 
including binary, JSON, and XML.
"""

import pickle
import json
import xml.etree.ElementTree as ET

def serialize(data, serialization_format):
    """
    Serializes the given dictionary into the specified format.

    Args:
        data (dict): The dictionary to serialize.
        serialization_format (str): The format to serialize the data into ('binary', 'json', 'xml').

    Returns:
        bytes: The serialized data.
    """
    if serialization_format == "binary":
        return pickle.dumps(data)
    elif serialization_format == "json":
        return json.dumps(data).encode()
    elif serialization_format == "xml":
        root = ET.Element("root")
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        return ET.tostring(root)
    else:
        raise ValueError("Invalid serialization format")
