# SEL0456
Repositório para os projetos da disciplina SEL0456 - Técnicas em Desenvolvimento de Software Livre

## Organização do Repositório
- **Teste**
  
  Diretório criado para testes realizados em aula.
  
- **Trabalho1**

  Diretório referente à entrega do Trabalho 1.

- **Trabalho2**

  Diretório referente à entrega do Trabalho 2.

- **Trabalho3**

  Diretório referente à entrega do Trabalho 3.

## Funcionalidade dos Projetos

### Trabalho 1

  Este projeto consiste de um arquivo principal (_main.c_) localizado na pasta _/src_, o qual irá executar 3 funções distintas localizadas em arquivos .c distintos. Para isso, é utilizado um arquivo _Makefile_ para a compilação e controle do projeto. As funções implementadas foram:
  - ```make```: Responsável pela compilação do projeto e criação do programa main.
  - ```make run```: Responsável por executar o programa main.
  - ```make clean```: Responsável por excluir os arquivos binários criados durante a compilação.
  - ```make distclean```: Responsável por excluir o programa main.

### Trabalho 2
  Este projeto consiste em uma implementação de uma classe em pyhton para controle de usuários (_users.py_) e de um arquivo exemplificando sua utilização (_app.py_). Os atributos e métodos desta classe são:
  - Atributos:
    - ```User.username```: Nome do usuário;
    - ```User.role```: Cargo do usuário (superadmin, admin ou user). Não pode ser alterado;
    - ```User.password_hash```: Hash da senha do usuário. Não pode ser diretamente alterado.
  - Métodos:
    - ```User.verify_password(password)```: Verifica se a senha enviada equivale à senha do usuário;
    - ```User.change_password(old_password, new_password)```: Muda a senha do usuário caso senha atual do usuário informada esteja correta.
  
  Para visualizar o caso teste basta executar o arquivo _app.py_ com um interpretador python.

### Trabalho 3
  Este projeto conciste na aplicação do GitHub Actions, utilizando o python application para realizar testes do arquivo _main.py_. Para melhor entendimento, observar as seguintes _branches_:
  - **project3-branch1**:
    Nesta branch é utilizado o comando python para executar o arquivo _main.py_, o qual retorna a senha contida no arquivo _password_entry.txt_ e compara a mesma com a senha presente no arquivo _password_hash.txt_. O resultado da comparação também é retornado;
  - **project3-branch2**:
    Nesta branch é utilizado o pytest para o teste do arquivo _main.py_. Para isso, é realizado um teste comparando a senha presente no arquivo _password_entry.txt_ com a senha do arquivo _password_hash.txt_, por meio da função ```verify_password()```.
    
  As funções presentes no arquivo function são:
  - ```hash_password()```: responsável por criptografar a senha utilizando sha256;
  - ```verify_password()```: responśavel por comparar as senhas, retornando _True_ ou _False_.
