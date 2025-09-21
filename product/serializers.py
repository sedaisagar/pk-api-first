from rest_framework import serializers


from product.models import Product

import hmac
import hashlib
import base64
import time

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

    def to_representation(self, instance:Product):
        data =  super().to_representation(instance) 
        transaction_uuid = f"{instance.id}-" + str(int(time.time()))
        signature = self.generate_signature(instance.price,transaction_uuid)
        data["signature"] = signature
        data["transaction_uuid"] = transaction_uuid
        return data