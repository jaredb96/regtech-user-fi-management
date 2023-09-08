from typing import List, Optional

from fastapi import Query


def parse_leis(leis: List[str] = Query(None)) -> Optional[List]:
    """
    Parses leis from list of one string to list of multiple distinct lei strings
    Returns empty list when nothing is passed in
    Ex: ['lei1,lei2'] -> ['lei1', 'lei2']
    """

    if leis is None or len(leis) == 0 or leis[0] == "":
        return []
    else:
        return leis[0].split(',')