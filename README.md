# Murph

Dashboard de notícias, clima, ações e informações de desempenho do computaodr, feito em HMTL, CSS e JavaScript e com a integração com Python pela biblioteca EEL. Além disso, o programa é desbloqueado por reconhecimento facial, utilizando a biblioteca OpenCV. 

![](https://i.ibb.co/t8Y3y13/gif-murph.gif)

[Interface](#interface)<br>
[Reconhecimento Facial](#reconhecimento-facial)<br>
[Funcionalidades](#funcionalidades)<br>

## Interface

Para a interface realizada, foi utilizado a biblioteca [EEL](https://pypi.org/project/Eel/), a qual realiza a integração entre o Python com as tecnologias Web, com a finalidade de construir uma aplicação Desktop. Diante disso, é visto a facilidade do desenvolvimento de aplicações que exigem designs mais complexos e com animações e integrações com outros meios (como o Chart.js, utilizado para os gráficos).

Portanto, a aplicação foi construída com HTML, CSS e manipulação por JavaScript, de tal forma, foi possível realizar todas as animações de forma dinâmica e funcional.

Para os gráficos, foi utilizado o [Chart.js](https://www.chartjs.org/), o qual as animações e a construção dos gráficos é de sua responsabilidade, tornando simples sua utilização.

## Reconhecimento Facial

O reconhecimento facial foi feito com a biblioteca OpenCV a partir da classificação do tipo LBPH, que sua função é rotular os pixels de uma imagem ao limitar a vizinhança de cada pixel e considera o resultado como um número binário. Por meio disso, foi criado dois arquivos, o de [captura de fotos](/capture.py) e o de [treinamento](/training.py) do modelo.

A partir disso, o algoritmo identifica as diferentes pessoas da captura por um id, localizado no nome da imagem, e no treinamento classifica os indivíduos com base nesse identificador. E com base nele, é relacionado com o nome da pessoa que já está pré determinado.

## Funcionalidades
