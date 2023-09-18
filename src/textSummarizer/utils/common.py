import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.

    Parameters
    ----------
    path_to_yaml : Path
        Path to the YAML file.

    Returns
    -------
    ConfigBox
        A ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            try:
                return ConfigBox(yaml.safe_load(yaml_file))
            except yaml.YAMLError as exc:
                logger.error(exc)
                raise BoxValueError(exc)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path_to_yaml} not found")
    except PermissionError:
        raise PermissionError(f"File {path_to_yaml} is not readable")
    except Exception as exc:
        logger.error(exc)
        raise
    

@ensure_annotations
def create_directories(path_to_dirextories: list, verbose=True):
    """
    Create directories if they do not exist.

    Parameters
    ----------
    path_to_dirextories : list
        List of directories to create.
    verbose : bool, optional
        Whether to print a message. The default is True.

    Returns
    -------
    None.
    """
    for directory in path_to_dirextories:
        if not os.path.exists(directory):
            if verbose:
                logger.info(f"Creating directory {directory}")
            os.makedirs(directory)
        else:
            if verbose:
                logger.info(f"Directory {directory} already exists")
                
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file.

    Parameters
    ----------
    path : Path
        Path to the file.

    Returns
    -------
    str
        The size of the file.
    """
    size = os.path.getsize(path)
    if size < 1024:
        return f"{size} bytes"
    elif size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 ** 3:
        return f"{size / 1024 ** 2:.2f} MB"
    elif size < 1024 ** 4:
        return f"{size / 1024 ** 3:.2f} GB"
    else:
        return f"{size / 1024 ** 4:.2f} TB"