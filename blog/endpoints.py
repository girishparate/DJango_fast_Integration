from typing import Any, List
from fastapi import APIRouter
from .api_crud import sample
from .schema import AllSampleList, SampleBase, CreateSample, UpdateSample, SampleOut, SampleListOut, SingleSample

router = APIRouter()

@router.get("/blogs/", response_model = List[AllSampleList])
def get_multiple_blog(offset:int =0, limit:int=10) -> Any:
    return sample.get_multiple(offset=offset, limit=limit)

@router.post("/blogs/", status_code=201, response_model=SingleSample)
def create_sample(request: CreateSample) -> Any:
    return sample.create(obj_in=request)

@router.get("/blogs/{id}/", response_model=SingleSample)
def get_sample(id: int) -> Any:
    return sample.get(id=id)

@router.put("/blog/{id}/", response_model=SingleSample)
def update_sample(id: int, request: UpdateSample) -> Any:
    return sample.update(id=id, obj_in=request)

@router.delete("/blogs/{id}/")
def delete_sample(id: int) -> Any:
    return sample.delete(id=id)

