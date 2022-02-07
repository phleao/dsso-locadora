Tema Livre (Sistema de Locação de Filmes) 
 
 
PROBLEMA: Implementar um sistema orientado a objetos em Python para gerenciamento de locações de filmes em um site. 
 
ESCOPO DO DESENVOLVIMENTO: O sistema permite o cadastro de filmes e pessoas e realiza locações. Cada filme possui título, sinopse, gênero, faixa etária e link de acesso. Já as pessoas, possuem nome, email e senha.

O sistema deve possuir todos os filmes cadastrados no catalogo da locadora (cadastrado por funcionários, subclasse de Pessoas, que possui CPF no cadastro), os locatários (outra subclasse de pessoas, que possui idade) e o histórico de locações.

O sistema registra a locação, que deve ser possuir um filme e um locatário e a data de locação, após finalizar a locação, deve avaliar o filme alugado. 

Cada usuário consegue visualizar seu histórico de locações, informações da locação atual (caso tenha), visualizar lista de filmes com melhores avaliações (que será gerada através de uma média aritmética da avaliação de todos os usuários que alugaram o filme) e comentários de outros usuários sobre os filmes do catalogo. 

Já os funcionários conseguem visualizar as locações ativas e inativas, o status de cada usuário e manipular todas as informações dos filmes.

REGRAS DE NEGÓCIO
1.	Somente usuários cadastrados podem alugar filme.
2.	Um usuário não consegue alugar mais de um filme ao mesmo tempo. Porém um filme pode ser alugado por diversas pessoas ao mesmo tempo.
3.	Usuário não pode alugar filmes indicados para uma idade maior que a dele.
4.	Não existem funcionário e cliente com mesmo email.
5.	A única função do funcionário é manipular os filmes, ou seja, não possui caminhos para manipular locações, clientes e avaliações.

RESTRIÇÕES DE ESCOPO: Para simplificar a implementação, a complexidade das regras e controles relacionados ao gerenciamento das locações, não será necessário efetuar pagamento para realizar o aluguel. 
 
DETALHAMENTO DA DIVISÃO DO TRABALHO: A nossa dupla é composta pelo João Zaniboni e pelo Pedro Leão. Decidimos dividir o trabalho entre, o João ficará responsável por implementar as classes e subclasses relacionadas à Pessoas (ou seja, funcionário e clientes) e as avaliações. Já o Pedro desenvolverá o cadastro de Filmes e Locações. Ademais, iremos desenvolver juntos as classes controladoras e telas.


João Victor Neves Zaniboni (21100505)
Pedro Henrique Leao Schiavinatto (21104935)