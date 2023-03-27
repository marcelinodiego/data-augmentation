# UM ESTUDO SOBRE DIFERENTES APLICAÇÕES DAS TÉCNICAS DE DATA AUGMENTATION PARA UM CONJUNTO DE DADOS LIMITADO

Tabela de conteúdos
=================
<!--ts-->
   * [Tabela de Conteudo](#tabela-de-conteudo)
   * [Descrição do Projeto](#descricao-do-projeto)
   * [Status do projeto](#status-do-projeto)
   * [Como usar](#como-usar)
   * [Métodos de Aumento Aplicados e Demonstração](#metodos-aplicados)
   * [Tecnologias](#tecnologias)
   * [Autor](#autor)
<!--te-->

# Descrição do projeto

Esse projeto foi desenvolvido para explorar as técnicas de aumento de dados como uma alternativa para solucionar o problema da limitação dos dados, seja pela pouca quantidade de exemplos disponíveis, falta de profissionais capacitados para rotulagem ou necessidade de autorização para seu uso. O algoritmo recebe como entrada um conjunto de dados composto por imagens no formato PNG(Portable Network Graphics), executa os métodos de aumento para cada imagem que compõe o banco e retorna um conjunto de dados expandido.   

# Status do projeto

- Finalizado :chart:

# Como usar

Considerando que já tenha instalado as dependências da seção (#tecnologias) .Esse projeto é composto por duas funções 'PadronizacaoFormato' e 'main'.

PadronizacaoFormato -  Função auxiliar responsável por converter o formato das imagens para PNG(Portable Network Graphics), caso não estejam nele.

main - Função principal que realiza o aumento de dados propriamente dito.

A função PadronizacaoFormato pode ser executada da seguinte forma:
- Recebe como entrada imagens que estejam em qualquer formato dentro de uma pasta como nome 'ImagensOriginais';
- Caso não exista, criar uma pasta com o nome 'ImagensPadronizadas' para receber as imagens com formato modificado. 

A função main possui alguns requisitos e detalhes que precisam ser salientados para sua correta execucação:
- Recebe imagens apenas no formato PNG;
- As imagens de entrada precisam estar numa pasta com nome 'ImagensPadronizadas';
- Caso não exista, criar uma pasta com nome 'aumento_dados' para receber as novas imagens geradas.

# Métodos de Aumento Aplicados e Demonstração

# Tecnologias

As seguintes ferramentas foram utilizadas na construção desse projeto:

- [Python](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/install?hl=pt-br)
- [Keras](https://keras.io/)
- [Skimage](https://scikit-image.org/docs/stable/install.html)
- [OS](https://www.python.org/)
- [OpenCV](https://pypi.org/project/opencv-python/)

# Conclusão

# Autor
- [Diêgo Marcelino Santos Silva](https://github.com/marcelinodiego)
