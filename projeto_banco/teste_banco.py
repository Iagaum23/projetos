from models.conta import Conta
from models.cliente import Cliente

iago: Cliente = Cliente('Iago', 'Barbosa', 'iagofbarbosa23@gmail.com', '138.113.137-97', '26/12/2002')
felicity: Cliente = Cliente('Felicity', 'Jones', 'felicityJones@gmail.com', '041.680.850-66', '14/05/2006')

conta1: Conta = Conta(iago)
conta2: Conta = Conta(felicity)

print(conta1.depositar(100))
print(conta2.depositar(100))
print(conta1.transferir(conta2, 50))
print(conta1.extrato)
print(conta2.extrato)
