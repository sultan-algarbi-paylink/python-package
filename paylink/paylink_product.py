from typing import Optional, Dict, Any


class PaylinkProduct:
    def __init__(
        self,
        title: str,
        price: float,
        qty: int,
        description: Optional[str] = None,
        is_digital: bool = False,
        image_src: Optional[str] = None,
        specific_vat: Optional[float] = None,
        product_cost: Optional[float] = None,
    ):
        self.title = title
        self.price = price
        self.qty = qty
        self.description = description
        self.is_digital = is_digital
        self.image_src = image_src
        self.specific_vat = specific_vat
        self.product_cost = product_cost

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "price": self.price,
            "qty": self.qty,
            "description": self.description,
            "isDigital": self.is_digital,
            "imageSrc": self.image_src,
            "specificVat": self.specific_vat,
            "productCost": self.product_cost,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            price=data.get("price", 0.0),
            qty=data.get("qty", 0),
            description=data.get("description", ""),
            is_digital=data.get("isDigital", False),
            image_src=data.get("imageSrc", ""),
            specific_vat=data.get("specificVat", None),
            product_cost=data.get("productCost", None),
        )
