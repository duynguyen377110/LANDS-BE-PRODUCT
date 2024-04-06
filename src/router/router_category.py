from flask import Blueprint, request
from src.controller.controller_category import ControllerCategory
from src.utils.util_db import UtilDb

router_category = Blueprint("category", __name__)
controllerCategory = ControllerCategory()
utilDb = UtilDb()

@router_category.post("/api/v1/category")
def create_category():
    body = request.data.decode("utf-8")
    return controllerCategory.create_category(body)

@router_category.patch("/api/v1/category")
def update_category():
    body = request.data.decode("utf-8")
    return controllerCategory.update_category(body)

@router_category.delete("/api/v1/category")
def delete_category():
    body = request.data.decode("utf-8")
    return controllerCategory.delete_category(body)