from flask import Blueprint, request
from src.controller.controller_product import ControllerProduct

router_product = Blueprint("product", __name__)
controllerProduct = ControllerProduct()

@router_product.post("/api/v1/product")
def create_product():
    body = request.data.decode("utf-8")
    return controllerProduct.create_product(body)

@router_product.patch("/api/v1/product")
def update_product():
    body = request.data.decode("utf-8")
    return controllerProduct.update_product(body)


@router_product.delete("/api/v1/product")
def delete_product():
    body = request.data.decode("utf-8")
    return controllerProduct.delete_product(body)