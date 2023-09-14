import logging
import os

def lambda_handler(event: str, context: int) -> str:
    if type(context) != int:
        return None
    
    print(4)
    return event + str(context)


