from django.db import transaction
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException
from products.models import Product
from .models import Redemption

def redeem_product(user, product_id):
    # transaction 保證資料一致
    with transaction.atomic():

        product = get_object_or_404(Product, id=product_id)
        # 避免同時多人搶
        product = Product.objects.select_for_update().get(id=product_id)
        user = user.__class__.objects.select_for_update().get(id=user.id)

        if product.stock <= 0:
            raise APIException("商品已售完")

        if user.points < product.points_required:
            raise APIException("點數不足")


        # 扣點
        user.points -= product.points_required
        user.save()

        # 扣庫存
        product.stock -= 1
        product.save()

        # 建立紀錄
        Redemption.objects.create(user=user, product=product)