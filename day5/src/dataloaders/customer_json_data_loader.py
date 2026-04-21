# create customer json data loader implementation from customer data loader abstract class
import json
from models.customer import Customer
from models.full_name import FullName
from dataloaders.customer_data_loader import CustomerDataLoader
from stores.customer_store_impl import CustomerStoreImpl


class CustomerJSONDataLoader(CustomerDataLoader):

    def load_data(self, file_path: str, customer_store: CustomerStoreImpl):
        with open(file_path, 'r') as file:
            data = json.load(file)

        for item in data:
            customer_id = int(item['customer_id'])
            first_name = item['first_name']
            last_name = item['last_name']
            email = item['email']
            phone_no = item['phone_no']

            full_name = FullName(
                first_name=first_name,
                last_name=last_name
            )

            customer = Customer(
                customer_id=customer_id,
                name=full_name,
                email=email,
                phone_no=phone_no
            )

            customer_store.add_customer(customer)
