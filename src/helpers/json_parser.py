import json
from typing import Tuple


def read_deploy(file) -> Tuple[list, str, list, list, dict]:
    """Parses and verifies fields for deploy operations"""
    with open(file) as f:
        d = json.load(f)
        try:
            targets = d["targets"]
            path_to_application = d["path_to_application"]
            add_packages = d["add_packages"]
            delete_packages = d["delete_packages"]
            metadata = d["metadata"]
            return targets, path_to_application, add_packages, delete_packages, metadata
        except KeyError:
            print("ERROR: JSON is missing fields.")


def read_configure(file) -> Tuple[list, list, list, dict]:
    """Parses and verifies fields for configure operations"""
    with open(file) as f:
        d = json.load(f)
        try:
            targets = d["targets"]
            metadata = d["metadata"]
            add_packages = d["add_packages"]
            delete_packages = d["delete_packages"]
            return targets, add_packages, delete_packages, metadata
        except KeyError:
            print("ERROR: JSON is missing fields.")
