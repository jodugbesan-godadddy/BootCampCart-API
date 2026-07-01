import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseCartItem

class CartItem:
    def on_get(self, req, resp, cart_item_id):
        cart_item = DatabaseCartItem.get(id=cart_item_id)
        resp.media = model_to_dict(cart_item)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, cart_item_id):
        DatabaseCartItem.delete_by_id(cart_item_id)
        resp.status = falcon.HTTP_204

    def on_patch(self, req, resp, cart_item_id):
        cart_item_data = req.media
        DatabaseCartItem.update(**cart_item_data).where(
            DatabaseCartItem.id == cart_item_id
        ).execute()
        resp.status = falcon.HTTP_204
