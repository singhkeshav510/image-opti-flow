import logging
import os

def image_processor(event: str, context: int) -> str:
    if type(context) != int:
        return None
    return event + str(context)


