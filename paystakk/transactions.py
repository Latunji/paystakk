from paystakk.request import PaystackRequest
from paystakk.utils import build_params


class Transactions(object):
    def __init__(self, **kwargs):
        self.__base = PaystackRequest(**kwargs)
        self.__url = 'https://api.paystack.co/transaction/initialize'

    @property
    def ctx(self):
        return self.__base

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def customer_code(self):
        return self.ctx.data.get('access_code', '')

    @property
    def reference(self):
        return self.ctx.data.get('reference', '')

    def __getattr__(self, item):
        return getattr(self.__base, item)

    def create_customer(self, email, reference=None, amount=None, plan=none, sub_account=None, metadata=None,
                        transaction_charge=None,  invoice_limit=none, bearer=None, channels=channels):
        params = build_params(email=email, reference=reference,
                              amount=amount, plan=plan, sub_account=sub_account,
                              metadata=metadata, transaction_charge=transaction_charge, invoice_limit=invoice_limit,
                              bearer=bearer, channels=channels)

        self.ctx.post(self.url, json=params)

    def list_transactions(self, per_page=None, customer_id=None, page=None,
                          status=None, time_from=None, time_to=None, amount=None):
            params = build_params(
                perpage=per_page, customer_id=customer_id, page=page, status=status,
                time_from=time_from, time_to=time_to, amount=amount)
            self.ctx.get(self.url, listtransactions=params)

    def fetch_transactions(self, transaction_id):
        """
        If there is no customer that satisfies the `transaction_id`
        argument, it returns None

        :param transaction_id: An Id for the transaction to fetch
        :return: dict
        """
        url_ = '{url}/{id}'.format(url=self.url, id=transaction_id)
        self.ctx.get(url_)
