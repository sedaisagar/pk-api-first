from rest_framework import serializers
from core.settings import BASE_DIR

from PIL import Image
import time

# serializers.ModelSerializer
class IconSerializer(serializers.Serializer):
    file = serializers.ImageField()
    height = serializers.IntegerField(required=False)
    width = serializers.IntegerField(required=False)
    # accepts the input data
    # validation perform
    # perform create or update operation

    def to_representation(self, instance):
        return instance
    


    def create(self, validated_data):
        height = validated_data.get("height", 100)
        width = validated_data.get("width", 100)
        # Steps Performed
        image = validated_data["file"]
        image_name = image.name

        name_only = image_name.split(".")[0]
        # name : "abcasdfasdfasdf.jpg"
        # split : ["abcasdfasdfasdf", "jpg"]
        # [0]

        img = Image.open(image)
        file_name = f"{name_only}{time.time()}.ico"
        img.save(BASE_DIR / "media" / file_name, format='ICO',sizes=[(height, width)])
        
        return {"icon": f"http://localhost:8000/media/{file_name}", "height": height, "width": width}
    


    # Outgoing data
    # Single Data , or List of Data
    # In Individual data , serializer tries to get value from it


    # name, age, email (Required Fields)
    # {''name:'', 'age':0, 'email':''} => Valid
    
    # {'address':'', 'country':0} => Invalid