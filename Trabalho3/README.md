### Trabalho 3
  Este projeto conciste na aplicação do GitHub Actions, utilizando o python application para realizar testes do arquivo _main.py_. Para melhor entendimento, observar as seguintes _branches_:
  - **project3-branch1**:
    Nesta branch é utilizado o comando python para executar o arquivo _main.py_, o qual retorna a senha contida no arquivo _password_entry.txt_ e compara a mesma com a senha presente no arquivo _password_hash.txt_. O resultado da comparação também é retornado;
  - **project3-branch2**:
    Nesta branch é utilizado o pytest para o teste do arquivo _main.py_. Para isso, é realizado um teste comparando a senha presente no arquivo _password_entry.txt_ com a senha do arquivo _password_hash.txt_, por meio da função ```verify_password()```.
    
  As funções presentes no arquivo function são:
  - ```hash_password()```: responsável por criptografar a senha utilizando sha256;
  - ```verify_password()```: responśavel por comparar as senhas, retornando _True_ ou _False_.
