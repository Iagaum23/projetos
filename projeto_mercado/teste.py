import unittest
from models.produtos import Produtos
from mercado import *


class TesteProjeto(unittest.TestCase):

    def setUp(self):
        produto = Produtos('Ryzen 5 1600AF', 50, 750.00, 1399.90)
        produto2 = Produtos('Ryzen 5 3600X', 100, 900.00, 1599.90)
    
    def test_venda(self: object):
        mercado.venda()
    