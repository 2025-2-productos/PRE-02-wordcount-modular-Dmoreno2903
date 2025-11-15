def read_all_lines(folder: str, file: str) -> list[str]:
    """Read all the lines from a file
    
    Args:
        file: the file to read the lines from
        
    Returns:
        list of lines
    """
    with open(f"{folder}/{file}", "r") as f:
        lines: list[str] = f.readlines()
    return lines