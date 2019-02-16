# ARX Technologies Website

Our official website which we sell our custom made products. Customers can select features as they wish and give an order.

## Getting Started

We used Django web framework to develop our site.

### Prerequisites

What things you need to install are:
* Python3
* Django


### How To Create a Product From Console?

A step by step series of examples that tell you how to create and publish a product.<br>

1) Import necessary libraries.

```
from products.models import Choice, Product
```

2) Now we can create a product object.

```
hamburger = Product(product_text = "Delicious Hamburger", product_price = 10, product_tag = "Food")
```

And that's all you need to know!

### How To Create a Feature From Console?

A step by step series of examples that tell you how to create a feature and connect it to product.<br>

1) Import necessary libraries.

```
from products.models import Choice, Product
```

2) Now we can create a feature object.

```
hamburger.choice_set.create(feature_text = "Body: Extra Meat Balls", feature_stock = 100, feature_price = 2, product_images = "delicious-hamburger.png")
```

And that's it!

## Deployment

We use pythonanywhere.com to serve our website.

## Built With

* [Django Web Framework](https://www.djangoproject.com/) - The web framework used
* [Pythonanywhere](https://www.pythonanywhere.com) - Hosting Service

## Little Trip

* How about stop reading and start to check out our website?

![1](https://user-images.githubusercontent.com/30238276/52897288-d60ca180-31e3-11e9-831c-78c327566050.PNG)
![2](https://user-images.githubusercontent.com/30238276/52897289-d60ca180-31e3-11e9-9e6b-47aad547f333.PNG)
![3](https://user-images.githubusercontent.com/30238276/52897290-d60ca180-31e3-11e9-882c-10b602b6baf9.PNG)
![4](https://user-images.githubusercontent.com/30238276/52897291-d6a53800-31e3-11e9-8c6d-bfa96020ec84.PNG)
![5](https://user-images.githubusercontent.com/30238276/52897292-d6a53800-31e3-11e9-80e1-4dfb8b5c23a1.PNG)
![6](https://user-images.githubusercontent.com/30238276/52897293-d6a53800-31e3-11e9-8c70-95e19b3ce98d.PNG)
![7](https://user-images.githubusercontent.com/30238276/52897287-d60ca180-31e3-11e9-8019-710cff961341.PNG)
