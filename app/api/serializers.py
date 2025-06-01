from rest_framework import serializers
from app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ["id", "name", "description"]
        # exclude = ["id"]  # if you want to exclude the id field


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     view_name="Watch-Detail",
    #     many=True,
    #     read_only=True,
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"


# def get_len_name(self, obj):
#     return len(obj.title)

# def validate(self, data):
#     if data["title"] == data["storyline"]:
#         raise serializers.ValidationError("Title and storyline cannot be the same")
#     return data


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name must be at least 2 characters long")
#     return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     #######---- validators ----#######
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name must be at least 2 characters long")
#     #     return value

#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Name and description cannot be the same")
#         return data
