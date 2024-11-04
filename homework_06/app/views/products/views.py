from http import HTTPStatus

from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
)
from werkzeug.exceptions import (
    NotFound,
)

from models import Product
from .crud import products_storage as storage

products_app = Blueprint("products_app", __name__)


@products_app.get("/", endpoint="list")
def get_products():
    # products = Product.query.all()
    # products = storage.get()
    return render_template(
        "list.html",
        # products=products,
        products=storage.get(),
    )


@products_app.route("/add/", endpoint="add", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template(
            "add.html",
        )

    # if not form.validate_on_submit():
    #     return (
    #         render_template(
    #             "add.html",
    #         ),
    #         HTTPStatus.UNPROCESSABLE_ENTITY,
    #     )

    product_name = request.form.get("product-name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("product-name is requred")
    product = storage.create(name=product_name)
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product(product_id: int):
    product = storage.get_by_id(product_id)
    if product is None:
        raise NotFound(f"Product with id #{product_id} not found!")

    return render_template(
        "details.html",
        product=product,
    )


# @products_app.route(
#     "/<int:product_id>/confirm-delete/",
#     methods=["GET", "POST"],
#     endpoint="delete",
# )
# def delete_product(product_id: int):
#     product = Product.query.get_or_404(
#         ident=product_id,
#         description=f"Product with id #{product_id} not found!",
#     )


#     storage.delete(product)
#     return redirect(url_for("products_app.list"))