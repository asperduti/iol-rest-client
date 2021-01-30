import requests
import datetime

DEFAULT_API_VERSION = 'v2'
DOMAIN = 'api.invertironline.com'

class RestClient():
    """ RestClient instance that interacts with the InvertirOnline REST API."""

    def __init__(self, username, password):
        """
        Instantiate a new RestClient.

        Args:
            username (str): Username for InvertirOnline.com account.
            password (str): Username for InvertirOnline.com account
        """

        self.username = username
        self.password = password

        self.credentials = {}

        self.session = requests.session()
        self.auth()

    def auth(self):

        # Remove credentials from previous auth
        self.session.headers.pop('Authorization', None)
        
        payload = {
            'Host': DOMAIN,
        }
        
        # Try to refresh token if possible
        refresh_token = self.credentials.get("refresh_token", None)
        refresh_expires = self.credentials.get(".refreshexpires", None)
        if refresh_expires:
            refresh_expires = datetime.datetime.strptime(refresh_expires, '%a, %d %b %Y %H:%M:%S %Z')
        

        if refresh_token and datetime.datetime.utcnow() < refresh_expires:
            payload.update({
                'refresh_token': refresh_token,
                'grant_type': "refresh_token"
            })
        else:
            payload.update({
                'username': self.username,
                'password': self.password,
                'grant_type': "password"
            })

        response = self.__api_request(method="POST", url=self.__url("token"), data=payload)
        data = response.json()
        self.credentials.update(data)

        headers = {
            'Accept': 'text/json',
            'Authorization': "Bearer {token}".format(token=self.credentials["access_token"]),
            'Content-Type': 'application/json'
        }

        self.session.headers.update(headers)
        
        return

    def get_estado_cuenta(self):
        """ Retrieve the account status.

        Returns:
            dict: The JSON response
        """
        response = self.__api_request(method="GET",url=self.__url("estadocuenta"))
        return response.json()

    def get_portafolio(self, pais=None):
        """ Retrieve the porfolio by country.
        Args:
            pais (str): The country portfolio, it can be ['estados_Unidos', 'argentina'].

        Returns:
            dict: The JSON response
        """
        
        if pais is None:
            pais = "argentina"

        response = sself.__api_request(method="GET",url=self.__url("portafolio/{}".format(pais)))

        return response.json()

    def get_operaciones(self):
        """ Retrieve a list of operations.

        Args:
            # TODO: Complete arguments and filters

        Returns:
            list: List of operations
        """
        payload = {
            "filtro.fechaDesde": "2012-03-19T07:22Z",
        }

        response = self.__api_request(method="GET",url=self.__url("operaciones"), params=payload)

        return response.json()

    def get_operacion(self, numero):
        """ Retrieve detailed information of an operation
        Args:
            numero (int): Number operation.

        Returns:
            dict: The JSON response
        """
        response = self.__api_request(method="GET",url=self.__url("operaciones/{numero}".format(numero=numero)))
        return response.json()

    def delete_operacion(self, numero):
        """ Delete an operacion.
        Args:
            numero (int): Number operation.

        Returns:
            dict: The JSON response
        """
        response = self.__api_request(method="DELETE", url=self.__url("operaciones/{numero}".format(numero=numero)))
        return response.json()

    def comprar(self, mercado, simbolo, cantidad, precio, plazo, validez):
        """ Perform a 'Comprar' request.
        
        Args:
            mercado (str): The market can be one of ['bCBA', 'nYSE', 'nASDAQ', 'aMEX', 'bCS', 'rOFX'],
            simbolo (str): The ticker name
            cantidad (int): Quantity
            precio (float): The price
            plazo (str): It can be one of ['t0', 't1', 't2']
            validez (string): The date and time when the order expires.

        Returns:
            dict: The JSON response
        """
        return self.__operar("Comprar", mercado, simbolo, cantidad, precio, plazo, validez)

    def vender(self, mercado, simbolo, cantidad, precio, plazo, validez):
        """ Perform a 'Vender' request.
        
        Args:
            mercado (str): The market can be one of ['bCBA', 'nYSE', 'nASDAQ', 'aMEX', 'bCS', 'rOFX'],
            simbolo (str): The ticker name
            cantidad (int): Quantity
            precio (float): The price
            plazo (str): It can be one of ['t0', 't1', 't2']
            validez (string): The date and time when the order expires.

        Returns:
            dict: The JSON response
        """
        return self.__operar("Vender", mercado, simbolo, cantidad, precio, plazo, validez)

    def __api_request(self, method, url, retry=True, **kwargs):
        """ Utility method to perform call to InvertirOnline.com.
        
        Args:
            method (str): a REST method ['GET', 'POST', 'DELETE'].
            url (str):
            retry (bool): Try if returns status code 401.
            **kwargs: Arbitrary keyword arguments accepted by requests.request.

        Returns:
            dict: The JSON response
        """
        response = self.session.request(method, url, **kwargs)

        if response.status_code == 401:
            if retry:
                self.auth()
                response = self.__api_request(method, url, retry=False, **kwargs)

        return response

    def __operar(self, operacion, mercado, simbolo, cantidad, precio, plazo, validez):
        """ Utility method to operate('Comprar' or 'Vender')
        
        Args:
            operacion (str): Operation can be one of ['Comprar', 'Vender'].
            mercado (str): The market can be one of ['bCBA', 'nYSE', 'nASDAQ', 'aMEX', 'bCS', 'rOFX'],
            simbolo (str): The ticker name
            cantidad (int): Quantity
            precio (float): The price
            plazo (str): It can be one of ['t0', 't1', 't2']
            validez (string): The date and time when the order expires.

        Returns:
            dict: The JSON response
        """
        
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "plazo": plazo,
            "validez": validez
        }

        response = self.__api_request(method="POST",url=self.__url("operar/{operacion}".format(operacion=operacion)), json=data)
        return response.json()

    def __url(self, path):
        """ Utility method to build URL.
        
        Args:
            path (str): endpoint without api/{version}.
        
        Returns:
            str: The full URL
        """
        if path != "token":
            path = "api/{version}/{path}".format(version=DEFAULT_API_VERSION, path=path)

        return 'https://{domain}/{path}'.format(domain=DOMAIN, path=path)