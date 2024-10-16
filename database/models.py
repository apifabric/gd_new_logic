# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 16, 2024 16:06:37
# Database: sqlite:////tmp/tmp.ddJ7UVdwWc/gd_new_logic/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    """
    description: Defines product categories.
    """
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Customer(SAFRSBaseX, Base):
    """
    description: Represents a customer with a tracking balance for their orders.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    balance = Column(Float, nullable=False)
    credit_limit = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    AddresList : Mapped[List["Addres"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class OrderStatu(SAFRSBaseX, Base):
    """
    description: Tracks the status of orders in the system.
    """
    __tablename__ = 'order_status'
    _s_collection_name = 'OrderStatu'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    status_name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class PaymentMethod(SAFRSBaseX, Base):
    """
    description: Stores payment methods available to customers.
    """
    __tablename__ = 'payment_method'
    _s_collection_name = 'PaymentMethod'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    method_type = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Product(SAFRSBaseX, Base):
    """
    description: Represents a product that can be ordered, with a set unit price.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")
    ItemList : Mapped[List["Item"]] = relationship(back_populates="product")



class Promotion(SAFRSBaseX, Base):
    """
    description: Manages promotional offers on products.
    """
    __tablename__ = 'promotion'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class ShippingMethod(SAFRSBaseX, Base):
    """
    description: Defines different shipping methods available for orders.
    """
    __tablename__ = 'shipping_method'
    _s_collection_name = 'ShippingMethod'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    method_name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Supplier(SAFRSBaseX, Base):
    """
    description: Represents suppliers of products.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Addres(SAFRSBaseX, Base):
    """
    description: Represents address details for customers for deliveries.
    """
    __tablename__ = 'address'
    _s_collection_name = 'Addres'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    address_line1 = Column(String, nullable=False)
    city = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("AddresList"))

    # child relationships (access children)



class Inventory(SAFRSBaseX, Base):
    """
    description: Maintains current stock levels of products.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents an order placed by a customer, includes a field for notes and tracking total amount.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    date_placed = Column(DateTime)
    date_shipped = Column(DateTime)
    amount_total = Column(Float, nullable=False)
    notes = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    ItemList : Mapped[List["Item"]] = relationship(back_populates="order")



class Item(SAFRSBaseX, Base):
    """
    description: Represents an item in an order, linking to both the product being ordered and the order itself.
    """
    __tablename__ = 'item'
    _s_collection_name = 'Item'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("ItemList"))
    product : Mapped["Product"] = relationship(back_populates=("ItemList"))

    # child relationships (access children)
