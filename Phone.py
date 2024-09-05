from Item import Item
import csv


class Phone(Item):
    def __init__(self, name: str, price: float, qty=0,broken=0):
        super().__init__(name, price, qty)

        self.broken=broken

        assert broken>=0,f'given broken items {broken} is not greater or equal to zero!'


    @classmethod
    def read_from_csv(cls):
        with open('items.csv','r') as f:
            reader= csv.DictReader(f)
            items=list(reader)

        for item in items:
            Phone(
                name=item.get('name'),
                price=float(item.get('price')),
                qty= int(item.get('quantity'))
            )