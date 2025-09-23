from rest_framework import serializers


from product.models import Product

import hmac
import hashlib
import base64
import time
import requests
import json

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def generate_signature(self, total_amount, transaction_uuid, product_code="EPAYTEST"):
        parameters = f"total_amount={total_amount:.2f},transaction_uuid={transaction_uuid},product_code={product_code}".encode('utf-8')
        secret = '8gBm/:&EnhH.1/q'.encode('utf-8')
        hmac_sha256 = hmac.new(secret, parameters, hashlib.sha256)
        digest = hmac_sha256.digest()
        signature = base64.b64encode(digest).decode('utf-8') 
        print("Generated Signature:", signature)
        return signature
        # secret

    def generate_khalti_payment_link(self, amount, purchase_order_id, purchase_order_name):
        url = "https://dev.khalti.com/api/v2/epayment/initiate/"
        return url
        payload = json.dumps({
            "return_url": "http://localhost:8001/payment-success/",
            "website_url": "http://localhost:8001/payment-failure/",
            "amount": amount,
            "purchase_order_id": purchase_order_id,
            "purchase_order_name": purchase_order_name,
        })
        headers = {
            'Authorization': 'key 01fe9b9e699044f4a9c015622cc6e18e',
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json() 

        print("Khalti Response:", response_data)

        return response_data.get("payment_url", "")

    def to_representation(self, instance:Product):
        data =  super().to_representation(instance) 
        transaction_uuid = f"{instance.id}-" + str(int(time.time())) # This is unique in every cases
        signature = self.generate_signature(instance.price,transaction_uuid)
        data["signature"] = signature
        data["transaction_uuid"] = transaction_uuid
        
        khalti_link = self.generate_khalti_payment_link(instance.price * 100,transaction_uuid, instance.title )
        data["khalti_link"] = khalti_link
        return data

        """?pidx=QjhFLKtysuKvRRdrWx8DbW
        &transaction_id=hCNWYGHGLEzRuCVngV7KQg
        &tidx=hCNWYGHGLEzRuCVngV7KQg
        &txnId=hCNWYGHGLEzRuCVngV7KQg
        &amount=1200
        &total_amount=1200
        &mobile=98XXXXX005
        &status=Completed
        &purchase_order_id=1-1758553970
        &purchase_order_name=string"""

    # a => b => c =>  d => e

    # inst = Product()

    # # title, price, description, image
    # data = {
    #     "id": inst.id,
    #     "title": inst.title,
    #     "price": inst.price,
    #     "description": inst.description,
    #     "image": inst.image.url,
    #     # "signature": "generated_signature",
    #     # "transaction_uuid": "generated_uuid"
    # }