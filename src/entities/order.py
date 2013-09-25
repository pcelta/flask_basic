class Order(object):
   
    def __init__(self):
        self._partner                 = None
        self._email                   = None
        self._country                 = None
        self._sku                     = None
        self._login                   = None
        self._password                = None
        self._purchase                = None
        self._preference              = None
        self._product_type            = None
        self._msisdn                  = None
        self._start_date              = None
        self._end_date                = None
        self._contract_id             = None
        self._plan_code               = None
        self._action                  = None
        self._customer_identification = None
        self._callback                = None
        self._result                  = None
        pass
        
    @property
    def partner(self):
        return self._partner

    @partner.setter
    def.partner(self, partner):
        self._partner = partner
        
    @property
    def email(self):
        return self._email

    @email.setter
    def.email(self, email):
        self._email = email    @propert
        
    @property
    def country(self):
        return self._country

    @country.setter
    def.country(self, country):
        self._country = country
        
    @property
    def sku(self):
        return self._sku

    @sku.setter
    def.sku(self, sku):
        self._sku = sku

    @property
    def login(self):
        return self._login

    @login.setter
    def.login(self, login):
        self._login = login
    
    @property
    def password(self):
        return self._password

    @password.setter
    def.password(self, password):
        self._password = password
        
    @property
    def purchase(self):
        return self._purchase

    @purchase.setter
    def.purchase(self, purchase):
        self._purchase = purchase
        
    @property
    def preference(self):
        return self._preference

    @preference.setter
    def.preference(self, preference):
        self._preference = preference
        
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def.product_type(self, product_type):
        self._product_type = product_type
        
    @property
    def msisdn(self):
        return self._msisdn

    @msisdn.setter
    def.msisdn(self, msisdn):
        self._msisdn = msisdn
        
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def.start_date(self, start_date):
        self._start_date = start_date
        
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def.end_date(self, end_date):
        self._end_date = end_date
        
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def.contract_id(self, contract_id):
        self._contract_id = contract_id
        
    @property
    def plan_code(self):
        return self._plan_code

    @plan_code.setter
    def.plan_code(self, plan_code):
        self._plan_code = plan_code
        
    @property
    def action(self):
        return self._action

    @action.setter
    def.action(self, action):
        self._action = action
        
    @property
    def customer_identification(self):
        return self._customer_identification

    @customer_identification.setter
    def.customer_identification(self, customer_identification):
        self._customer_identification = customer_identification

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def.callback(self, callback):
        self._callback = callback
        
    @property
    def result(self):
        return self._result
        
    @result.setter
    def result(self, result):
        if not isinstance(result, 'src.entities.result.Result')
            raise ValueError('Invalid Argument. Must Result instance')
        self._result = result
        
    @staticmethod
    def createByJson(self, json):
        if 
        
