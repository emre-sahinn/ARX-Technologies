from django.db import models


class Product(models.Model):
    product_text = models.CharField(max_length=200)
    product_text2 = models.CharField(max_length=200, default="")
    product_tag = models.CharField(max_length=200, default="")
    product_price = models.IntegerField(default=-1)
    product_image = models.CharField(max_length=200, default="")

    def pro_series(self):
        return self.product_price >= 500

    def __str__(self):
        return self.product_text


class Choice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.CharField(max_length=200, default="")
    feature_price = models.IntegerField(default=-1)
    feature_text = models.CharField(max_length=250, default="")
    product_images = models.CharField(max_length=200, default="")
    feature_stock = models.IntegerField(default=100)

    def __str__(self):
        return self.feature


class ShoppingCart(models.Model):
    product_name = models.CharField(max_length=200)
    product_order = models.CharField(max_length=250, default="")
    user_name = models.CharField(max_length=30, default="unknown")
    user_address = models.CharField(max_length=200, default="unknown")
    total_price = models.IntegerField(default=-1)
    payment_completed = models.BooleanField(default=False)
    order_completed = models.BooleanField(default=False)

    def __str__(self):
        if self.order_completed:
            return str("-Order Completed- " + self.product_name + "(" + self.user_name + ")")
        elif self.payment_completed:
            return str("--Payment Completed-- " + self.product_name + "(" + self.user_name + ")")
        else:
            return str(self.product_name + "(" + self.user_name + ")")

    class Meta:
        ordering = ('order_completed', '-payment_completed', )
