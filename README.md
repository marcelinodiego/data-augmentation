# UM ESTUDO SOBRE DIFERENTES APLICAÇÕES DAS TÉCNICAS DE DATA AUGMENTATION PARA UM CONJUNTO DE DADOS LIMITADO

Tabela de Conteúdos
=================
<!--ts-->
   * [Tabela de Conteúdos](#tabela-de-conteudo)
   * [Descrição do Projeto](#descricao-do-projeto)
   * [Status do Projeto](#status-do-projeto)
   * [Como usar](#como-usar)
   * [Métodos de Aumento Aplicados e Teste](#metodos-aplicados)
      * [Métodos de Aumento](#metodos-de-aumento)
      * [Teste](#teste)
   * [Tecnologias](#tecnologias)
   * [Conclusão](#conclusão)
   * [Autor](#autor)
<!--te-->

# Descrição do Projeto

Esse projeto foi desenvolvido para explorar as técnicas de aumento de dados como uma alternativa para solucionar o problema da limitação dos dados, seja pela pouca quantidade de exemplos disponíveis, falta de profissionais capacitados para rotulagem ou necessidade de autorização para seu uso. O algoritmo recebe como entrada um conjunto de dados composto por imagens no formato PNG(Portable Network Graphics), executa os métodos de aumento para cada imagem que compõe o banco e retorna um conjunto de dados expandido.   

# Status do Projeto

- Finalizado :chart:

# Como usar

Considerando que já tenha instalado as dependências da seção [Tecnologias](#tecnologias) .Esse projeto é composto por duas funções 'PadronizacaoFormato' e 'main'.

PadronizacaoFormato -  Função auxiliar responsável por converter o formato das imagens para PNG(Portable Network Graphics), caso não estejam nele.

main - Função principal que realiza o aumento de dados propriamente dito.

A função PadronizacaoFormato pode ser executada da seguinte forma:
- Recebe como entrada imagens que estejam em qualquer formato dentro de uma pasta como nome 'ImagensOriginais';
- Caso não exista, criar uma pasta com o nome 'ImagensPadronizadas' para receber as imagens com formato modificado. 

A função main possui alguns requisitos e detalhes que precisam ser salientados para sua correta execucação:
- Recebe imagens apenas no formato PNG;
- As imagens de entrada precisam estar numa pasta com nome 'ImagensPadronizadas';
- Caso não exista, criar uma pasta com nome 'aumento_dados' para receber as novas imagens geradas.

# Métodos de Aumento Aplicados e Teste

Esta seção está dividida em dois tópicos, o primeiro é responsável por apresentar as técnicas de aumento utilizadas e alguns esquemas para exemplifica-los. No segundo, temos o resultado da aplicação das técnicas de aumentos pelo algoritmo desta pesquisa para um conjunto de dados limitado.  

## Métodos de Aumento

As técnicas de aumento de dados usadas para essa pesquisa são baseadas em transformações geométricas, que permite modificações na forma, tamanho e posição de elementos dentro da imagem, e também transformações fotométricas, que alteram as propriedades das cores na imagem, através de mudanças nos valores dos pixels.

### Translação
Na translação a imagem é deslocada ao longo do eixo x ou eixo y, permitindo ir para esquerda (b), direita (c), acima (d) ou abaixo (e). 

<div align="center">
<img src="https://user-images.githubusercontent.com/56489559/228076566-3209aec4-d19f-48cd-a32e-33f4be1d3d19.png"width="500px"
</div>
![translation](https://user-images.githubusercontent.com/56489559/228076566-3209aec4-d19f-48cd-a32e-33f4be1d3d19.png)

Existem diferentes abordagens para aplicação da translação, pode ocorrer apenas com os deslocamentos citados anteriormente que foi a metodologia aplicada neste trabalho, como também realizar uma combinação entre eles.

### Espelhamento
Método que realiza espelhamento, girando a imagem em um eixo vertical ou horizontal, movendo linhas e colunas inteiras de pixels. No espelhamento vertical a inversão será no eixo horizontal, sendo (a) à imagem original, temos o resultado dessa manipulação em (b).

![espelhamento vertical](https://user-images.githubusercontent.com/56489559/228076484-66b66fc9-1a53-4687-8524-0be66c1956a7.png)

Em relação ao espelhamento horizontal a inversão dos valores de pixels ocorre no eixo vertical, gerando uma imagem como mostrado abaixo:

![espelhamento horizontal](https://user-images.githubusercontent.com/56489559/228076447-9da5d55d-0d83-4b87-a631-049c94e57a0b.png)

### Rotação

Técnica que modifica a imagem fazendo um rotacionamento no sentido horário (b) ou anti-horário (c) em um eixo de 1º e 359º. É importante ressaltar que dependendo do ângulo escolhido pode ocorrer perda de informação, por isso fixamos as modificações em ângulos de 90°.

![rotação](https://user-images.githubusercontent.com/56489559/228077172-f7242fb5-adf3-48fc-b12d-c364153c0490.png)

### Brilho Aleatório

Rotina responsável por alterar a imagem em diferentes níveis de iluminação, resultando em uma imagem mais clara (b) ou mais escura (c), quando comparado com a original (a).

![brightness](https://user-images.githubusercontent.com/56489559/228077077-367f009f-4cad-41c9-84e8-24d24806bb13.png)

Esse método recebe um valor delta para gerar imagens no intervalo fechado (-delta, delta), quanto mais próximo de 1.0 for esse valor, mais brilho receberá a imagem e quanto mais distante de 1.0, mais escura será a imagem.

### Zoom Aleatório

Essa técnica pode ser usada para ampliar ou diminuir a imagem aleatoriamente, nesta pesquisa apenas a ampliação (b) está sendo utilizada. 

![zoom-in](https://user-images.githubusercontent.com/56489559/228079175-fe6aa2ad-8402-4aec-98a8-c4a7fe2f1127.png).

Nesse método os números decimais negativos são responsáveis por realizar a ampliação da imagem, os valores definidos foram -0,2 e -0,4 que se referem a gerar imagens ampliadas no intervalo fechado que varia entre 20\% e 40\%.

## Teste


# Tecnologias

As seguintes ferramentas foram utilizadas na construção desse projeto:

- [Python](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/install?hl=pt-br)
- [Keras](https://keras.io/)
- [Skimage](https://scikit-image.org/docs/stable/install.html)
- [OS](https://www.python.org/)
- [OpenCV](https://pypi.org/project/opencv-python/)

# Conclusão

Neste estudo, foi proposto a exploração de métodos que realizam o aumento sintético de dados em um conjunto limitado composto por imagens microscópicas de sangue. Nosso experimento aumentou a quantidade de dados no conjunto de 558 imagens para 5022 imagens. Deixamos como trabalhos futuros a adição de mais métodos de \emph{Data Augmentation} como filtro gaussiano e contraste aleatório, para aumentar a variedade dos dados. Também a implementação de uma rede neural convolucional para identificação de células cancerígenas no conjunto de dados produzido nessa pesquisa, avaliar o impacto do aumento de dados em um ambiente com restrição de dados e comparar os resultados alcançados com trabalhos semelhantes encontrados na literatura. 


# Autor
- [Diêgo Marcelino Santos Silva](https://github.com/marcelinodiego)
