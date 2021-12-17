endereco = "rua das flores 72, apartamento 1002, Larangeiras, Rio de aneiro, RJ, 23440-120"

import re # regular expressiom -- RegEx 

# 5 digitos + hifen(opcional) + 3 digitos 

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #match
if busca:
    cep = busca.group()
    print(cep)

