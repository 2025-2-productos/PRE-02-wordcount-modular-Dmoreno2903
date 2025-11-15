import os


def preprocess_lines(folder: str) -> list[str]:
    """Return a list of lines from a folder
    
    Args:
        folder: the folder to return the lines from
        
    Returns:
        list of lines
    """
    files: list[str] = os.listdir(folder)
    if not files:
        raise ValueError("No files found in the folder")
    
    return files