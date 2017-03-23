/*Script para comprobar que el numero de instancias es de 1-99 y muestra un mensaje tipo span 
mostrando un error...*/
checkAlgorithm = () => {
  let nAlgorithms = document.getElementById('nAlgorithms').value;
  //comprueba mediante expresion regular si el numero de algoritmos esta entre 1-10
  if(nAlgorithms.match(/^([1-9]|10)$/)){
    $('#spanErrorAlgorithms').css('display', 'none');
    $('#nAlgorithms').css('color','inherit');
    $('#insertAlgorithm').show();
  }else{
    $('#nAlgorithms').css('color','#FF0000');
    $('#spanErrorAlgorithms').css('display', 'inherit');
    $('#insertAlgorithm').hide();
  }
}