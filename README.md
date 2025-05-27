# CINEMA VIRTUAL PROJETO LIVRE
(AL:RODRIGO DUTRA FERREIRA M:242015951)
-> O projeto que desenvolvi aborda um cinema virtual feito com python,
 onde um usuário Cliente ou usuário Administrador podem acessar. 

# UTILIZAÇÃO / CASOS DE USO
-> Execute o script principal main.py
A aplicação vai ser iniciada no terminal 

PASSO 1: LOGIN
# USUÁRIO ADMINISTRADOR:
-> Após escolher o login como administrador, o usuário deve 
fornecer :
- nome  
- cpf  
-carteirinha (que funciona como senha).
Se já houver uma conta de cpf e carteirinha fornecida cadastrada guardada em 
-packages/db/administrador.json 
o login será efetuado.

-> Credencial Padrão de Administrador: 
Nome: Rodrigo
cpf: 1234
carteirinha : 4321

# USUÁRIO CLIENTE:
-> Após escolher o login como Cliente, o usuário deve Fornecer:
- nome 
- cpf
dessa forma será criada uma conta para quaisquer credenciais adicionada.

PASSO 2: APÓS LOGIN
-> Após o login ser efetuado o usuário irá visualizar a área cinema onde há opções 
de 1 - 9 para escolher :

1)Adicionar Filme
-Exclusivo à Administradores
Administrador pode adicionar filmes pelo nome, genero e duração.

2)Adicionar Sessão
-Exclusivo à Administradores
Administrador pode adicionar sessões selecionando um filme e escolhendo horário.
Sessão será armazenada em
- packages/db/sessao.json

3)Listar Filmes
O usuário pode observar todos os filmes adicionados.

4)Listar Sessões 
O usuário pode observar todos as sessões adicionados.

5)Comprar Ingresso Para Sessão escolhida 
-Exclusivo à Clientes
Cliente pode comprar ingresso, visualizando as sessões disponiveis e escolhendo 
a que deseja comprar.O ingresso sera adicionado ao banco de dados junto com as credenciais do cliente em:
- packages/db/cliente.json

6)Listar Seus ingressos comprados
O usuário pode observar todos seus ingressos comprados.

7)Comprar na Lanchonete
O usuário pode comprar lanches, visualizando os produtos disponiveis e escolhendo o que deseja comprar.
O lanche comprado será removido de:
- packages/db/lanche.json

8)Adicionar produtos à lanchonete
-Exclusivo à Administradores
Administrador pode adcionar produtos à lanchonete oferecendo nome e preço do produto que quer adicionar, onde será armazenado em:
- packages/db/lanche.json

9)Sair
O usuario sai do menu fechando o terminal.