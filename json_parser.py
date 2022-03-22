import json
from typing import Tuple


def read_php_deploy(file) -> Tuple:
    with open(file) as f:
        d = json.load(f)
        targets = d["targets"]
        path_to_application = d["path_to_application"]
        add_packages = d["add_packages"]
        delete_packages = d["delete_packages"]
    return targets, path_to_application, add_packages, delete_packages
