import pytest

from src.image_opti_flow.lambda_scripts.image_processor import image_processor

@pytest.fixture
def event() -> str:
    return "Go Pro "

@pytest.mark.parametrize("context", [1, 2, "bro"])
def test_image_processor_method(event: str, context: int) -> None:
    result = image_processor(event, context)
    if type(context) == str:
        assert result == None
    else:
        assert result == event + str(context)