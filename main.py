import json
from datetime import datetime


class Transaction:
    def __init__(self, booking_date: str, partner_name: str, amount: int, reference: str, card: str):
        self.booking = datetime.strptime(
            booking_date, r'%Y-%m-%dT%H:%M:%S.%f%z')
        self.partner_name = partner_name
        self.amount = amount
        self.label = ''
        self.reference = reference
        self.card_number = card


def parse_erste_json(file_name: str) -> None:
    with open(file_name, encoding='utf-8') as json_file:
        raw_data = json.load(json_file)
    parsed_data = []
    for data in raw_data:
        parsed_data.append(Transaction(
            booking_date=data['booking'],
            partner_name=data['partnerName'],
            amount=data['amount']['value'],
            reference=data['reference'],
            card=data['cardNumber']))


if __name__ == '__main__':
    parse_erste_json('11600006-00000000-96619674_2021-11-01_2022-01-08.json')
