from inspect import ClassFoundException
from django.db.models import fields
from rest_framework import serializers
from core.models import Card, Cardinstance, User, Shop, Inventory, Guild, Shard

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields =  ['card_id', 'name', 'series', 'value']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'balance', 'created_at', 'capacity', 'suscription']

class CardInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardinstance
        fields = ['card_id', 'code_id', 'favorite', 'owner_id', 'number']

class ShardUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shard
        fields = ['status']

class ShardCloseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shard
        fields = ['status', 'shard_ping', 'shard_servers']
