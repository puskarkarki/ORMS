from django.db import models


# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=31, help_text='supplier name')
    address = models.CharField(max_length=31, help_text='address')
    phone = models.CharField(max_length=17, help_text='contact number')
    created_at = models.DateTimeField(auto_now=True)
    fax = models.CharField(max_length=17, help_text='fax number')
    email = models.EmailField(help_text='email_address')
    details = models.CharField(max_length=50, help_text='other details')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_supplier'
        verbose_name_plural = 'suppliers'
        ordering = ['-created_at']


class Product(models.Model):
    CATEGORY = (
        ('ED', 'Electronic Devices'),
        ('EA', 'Electronic Accessories'),
        ('HB', 'Health & Beauty'),
        ('BT', 'Baby & Toys'),
        ('GP', 'Groceries & Pets'),
        ('MF', 'Men Fashion'),
        ('WF', 'Woman Fashion'),
        ('SO', 'Sport Outdoor'),
    )

    PRICE_UNITS_CHOICES = (
        ('KG', 'Kilogram'),
        ('L', 'litre'),
        ('PCS', 'Pieces'),
        ('GM', 'Gram'),
        ('M', 'Metre'),
    )

    PRODUCT_STATUS = (
        ('A', 'Available'),
        ('NA', 'Not Available'),

    )

    name = models.CharField(max_length=31, help_text='name')
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=3, choices=PRICE_UNITS_CHOICES)
    category = models.CharField(max_length=3, choices=CATEGORY)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product_status = models.CharField(max_length=2, choices=PRODUCT_STATUS, default='A')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_products'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']


class Customer(models.Model):
    name = models.CharField(max_length=31, help_text='customer')
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=17, help_text='contact_number')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_customers'
        verbose_name_plural = 'Customers'
        ordering = ['-date_created']


class Order(models.Model):
    STATUS = (
        ('PD', 'Pending'),
        ('DLV', 'Delivered'),
        ('OFD', 'Out For Delivery'),
    )
    date_of_order = models.DateTimeField(auto_now_add=True)
    order_details = models.TextField()
    customer = models.ForeignKey(Customer, related_name="customer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS)

    def __str__(self):
        return self.order_details

    class Meta:
        db_table = 'tbl_order'
        verbose_name_plural = 'Order'
        ordering = ['-created_at']


class Payment(models.Model):
    PAYMENT_OPTIONS = (
        ('CD', 'Cash on Delivery'),
        ('GP', 'Google Pay'),
        ('AP', 'Amazon Pay'),
        ('MC', 'Master Card'),
        ('VSA', 'Visa Checkout'),

    )

    bill_no = models.CharField(max_length=7, primary_key=True)
    payment_options = models.CharField(max_length=3, choices=PAYMENT_OPTIONS)

    class Meta:
        db_table = 'payment_options'
        verbose_name_plural = 'Payment'
        ordering = ['-bill_no']


class OrderDetail(models.Model):
    SIZE = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),

    )
    price = models.DecimalField(max_digits=20, decimal_places=2)
    size = models.CharField(max_length=3, choices=SIZE)
    created_at = models.DateTimeField(auto_now=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="orders", on_delete=models.CASCADE)
    bill_no = models.ForeignKey(Payment, related_name="payment", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'order_detail'
        verbose_name_plural = 'OrderDetail'
        ordering = ['-created_at']
