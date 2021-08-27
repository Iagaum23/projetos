import unittest
from models.cliente import Cliente
from models.produtos import Produtos


class TesteProjeto(unittest.TestCase):

    def setUp(self):
        cliente = cliente.Cliente('Iago', 'Barbosa', 'iagofbarbosa23@gmail.com', '138.113.137-97', '26/12/2002')
