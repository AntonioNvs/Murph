// Determinando o tamanho máximo da janela
window.onresize = function (){
  if (window.outerWidth != 1080 || window.outerHeight != 768){
      window.resizeTo(1080, 768);
  }
}

// Quando a tela carregar, ative as funções de carregamento dos dados
window.onload = function () {
  eel.get_weather("init")
  eel.get_value_actions("init")
  eel.get_news("init")
  eel.recognition()
}

// Quando a face for detectada
eel.expose(modifyText)
function modifyText() {
  var text = document.getElementById('text')
  text.innerHTML = "Raciocinando.."
  text.setAttribute('data-text', "Raciocinando..")
}

// Indo para tela de dashboard
eel.expose(passName)
function passName() {
  window.location.replace('main.html')
}
