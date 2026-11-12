'''
Stimulate a basic e-commerce platform Where customers can browse products, add them to a cart, and place orders.
 Use OOP principles to manage inventory, pricing (for example, discounts), and order tracking.
 Integrate functionality for calculating taxes and shipping costs dynamically. 
'''
class Product:
    def __init__(self,product_id,name,price,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
    def display_details(self):
        print(f"[{self.product_id}] {self.name} - ${self.price} | Stock: {self.stock}")
class DiscountedProduct(Product):
    def __init__(self,product_id,name,price,stock,discount_percent):
        super().__init__(product_id,name,price,stock)
        self.discount_percent=discount_percent
    def get_final_price(self):
        return self.price*(1-self.discount_percent/100)
    def display_details(self):
        final_price=self.get_final_price()
        print(f"[{self.product_id}] {self.name} - ${self.price} (SALE: {self.discount_percent}% off -> ₹{final_price:.2f}) | Stock: {self.stock}")
class Cart:
    def __init__(self):
        # Dictionary mapping Product object -> quantity
        self.items={}
    def add_item(self,product,quantity):
        if product.stock>=quantity:
            if product in self.items:
                self.items[product]+=quantity
            else:
                self.items[product]=quantity
            print(f"Successfully added {quantity} x '{product.name}' to cart.")
        else:
            print(f"Sorry, not enough stock for '{product.name}'. Available: {product.stock}")
    def get_subtotal(self):
        subtotal=0
        for product,qty in self.items.items():
            if isinstance(product,DiscountedProduct):
                subtotal+=product.get_final_price()*qty
            else:
                subtotal+=product.price*qty
        return subtotal
    def display_cart(self):
        print("\n--- Your Shopping Cart ---")
        if not self.items:
            print("Your cart is empty.")
            return
        for product,qty in self.items.items():
            price_to_use=product.get_final_price() if isinstance(product,DiscountedProduct) else product.price
            print(f"- {product.name} * {qty} = ${price_to_use*qty:.2f}")
        print(f"Subtotal: ${self.get_subtotal():.2f}")
class Order:
    def __init__(self, order_id, customer_name, items, subtotal, tax, shipping, total):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.subtotal = subtotal
        self.tax = tax
        self.shipping = shipping
        self.total = total

    def print_receipt(self):
        print(f"\n======================================")
        print(f"RECEIPT FOR ORDER #{self.order_id}")
        print(f"Customer: {self.customer_name}")
        print(f"--------------------------------------")
        for product, qty in self.items.items():
            price = product.get_final_price() if isinstance(product, DiscountedProduct) else product.price
            print(f"  {product.name} (x{qty}): ₹{price * qty:.2f}")
        print(f"--------------------------------------")
        print(f"Subtotal: ₹{self.subtotal:.2f}")
        print(f"Tax (18%): ₹{self.tax:.2f}")
        print(f"Shipping: ₹{self.shipping:.2f}")
        print(f"TOTAL:    ₹{self.total:.2f}")
        print(f"======================================")
class ECommerceStore:
    def __init__(self,name):
        self.name=name
        self.catalog={}
        self.orders=[]
    def add_product(self,product):
        self.catalog[product.product_id]=product
    def display_catalog(self):
        print(f"\n--- {self.name} Product Catalog---")
        for product in self.catalog.values():
            product.display_details()
    def checkout(self,customer_name,cart):
        if not cart.items:
            print("Cannot checkout: Cart is empty.")
            return None
        for product,qty in cart.items.items():
            if product.stock<qty:
                print(f"Checkout failed: '{product.name}' is out of stock.")
                return None
        for product,qty in cart.items.items():
            product.stock-=qty
        subtotal=cart.get_subtotal()
        tax=subtotal*0.18
        shipping=0.0 if subtotal>=1000 else 50.0
        total=subtotal+tax+shipping

        order_id=len(self.orders)+1
        new_order=Order(order_id,customer_name,cart.items.copy(),subtotal,tax, shipping, total)
        self.orders.append(new_order)

        print(f"\nOrder placed successfully!")
        new_order.print_receipt()

        cart.items.clear()
        return new_order
my_store = ECommerceStore("Campus Bazaar")

p1 = Product("P1", "Notebook", 100.0, 50)
p2 = DiscountedProduct("P2", "Wireless Mouse", 800.0, 20, discount_percent=15)
p3 = DiscountedProduct("P3", "Coding T-Shirt", 500.0, 10, discount_percent=20)

my_store.add_product(p1)
my_store.add_product(p2)
my_store.add_product(p3)

my_store.display_catalog()

customer_cart = Cart()

customer_cart.add_item(p1, 3)  
customer_cart.add_item(p2, 1)  

customer_cart.display_cart()

my_store.checkout("Archana", customer_cart)

my_store.display_catalog()