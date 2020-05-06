from rest_framework import serializers
from comments.models import CommentReply, Comment
from users.serializers import UserDetailSerializer

class CommentUserSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer()
    reply_to = UserDetailSerializer()

    class Meta:
        model = CommentReply
        fields = "__all__"

class CommentReplySerializer(serializers.ModelSerializer):
    author = UserDetailSerializer()
    reply_to = UserDetailSerializer()

    class Meta:
        model = CommentReply
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    child_replys = CommentReplySerializer(many=True)
    author = UserDetailSerializer()

    class Meta:
        model = Comment
        fields = "__all__"


class CommentAddSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = "__all__"


class ReplyAddSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = CommentReply
        fields = "__all__"
