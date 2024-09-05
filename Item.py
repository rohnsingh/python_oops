import csv

class Item:
    discount=0.8
    all=[]

    def __init__(self,name:str,price:float,qty=0):

        #data quality checks on arguments
        assert price >=0,f'given price {price} is not greater or equal to zero!'
        assert qty >=0,f'given quantity {qty} is not greater or equal to zero!'
        
        #assign values to self object
        self.__name=name
        self.price=price
        self.qty=qty

        #add instances to list
        Item.all.append(self)

    @property
    # #@property= read only attribute
    def name(self):
        return self.__name

    def total_items_price(self):
        return self.price * self.qty
    
    def apply_discount(self):
        self.price=self.price*self.discount
     
    #format instance name to readable form 
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}",{self.price},{self.qty})'
    

    @classmethod
    def read_from_csv(cls):
        with open('items.csv','r') as f:
            reader= csv.DictReader(f)
            items=list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                qty= int(item.get('quantity'))
            )
        