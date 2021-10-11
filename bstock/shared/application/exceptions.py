from typing import Any, Sequence, Type
from pydantic import ValidationError, BaseModel, create_model
from pydantic.error_wrappers import ErrorList

ApplicationErrorModel: Type[BaseModel] = create_model("Application")

class NotFoundQueryError(ValidationError):
    def __init__(self, errors: Sequence[ErrorList], *, body: Any = None) -> None:
        self.body = body
        super().__init__(errors, ApplicationErrorModel)
