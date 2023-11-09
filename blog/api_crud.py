from typing import Generic, List, Optional, Type, TypeVar
from .base_crud import BaseCRUD
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model, Prefetch, query
from fastapi import Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from .models import Sample
from .schema import CreateSample, UpdateSample


class SampleCRUD(BaseCRUD[Sample, CreateSample, UpdateSample]):
    def get(self, id) -> Optional[Sample]:
        try:
            query = Sample.objects.get(id=id)
            return query
        except ObjectDoesNotExist:
            raise HTTPException(status_code=404, detail="This post is not exists.")

    def get_multiple(self, limit:int = 100, offset: int = 0) -> List[Sample]:
        query = Sample.objects.all()[offset:offset+limit]
        
        if not query:
            raise HTTPException(status_code=404, detail="There are not objects")

        return list(query)

    def create(self, obj_in: CreateSample) -> Sample:
        post = Sample.objects.filter(id=id)

        if not post:
            obj_in = jsonable_encoder(obj_in)
            query = Sample.objects.create(**obj_in)
        return query

    def update(self, obj_in: UpdateSample, id) -> Sample:
        self.get(id=id)

        if not isinstance(obj_in, list):
            obj_in = jsonable_encoder(obj_in)
        return Sample.objects.filter(id=id).update(**obj_in)

    def delete(self, id) -> Sample:
        self.model.objects.filter(id=id).delete()
        return {"detail": "Successfully deleted!"}

sample = SampleCRUD(Sample)