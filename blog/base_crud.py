from typing import Generic, List, Optional, Type, TypeVar
from django.db.models import Model
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Model)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)

class BaseCRUD(Generic[ModelType, CreateSchema, UpdateSchema]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, id) -> Optional[ModelType]:
        return self.model.objects.get(id=id)

    def get_multiple(self, limit:int = 100, offset:int = 0) -> List[ModelType]:
        return self.model.objects.all()[offset:offset+limit]

    def create(self, obj_in: CreateSchema) -> ModelType:
        if not isinstance(obj_in, list):
            obj_in = jsonable_encoder(obj_in)
        return self.model.objects.create(**obj_in)

    def update(self, obj_in: UpdateSchema, id) -> ModelType:
        if not isinstance(obj_in, list):
            obj_in = jsonable_encoder(obj_in)

        return self.model.objects.filter(id=id).update(**obj_in)

    def delete(self, id) -> ModelType:
        self.model.objects.filter(id=id).delete()
        return {"detail": "Successfully deleted!"}