/*Script para comprobar que el numero de instancias es de 1-99 y muestra un mensaje tipo span 
mostrando un error...*/
checkAlgorithm = () => {
  let nAlgorithms = document.getElementById('nAlgorithms').value;
  console.log(nAlgorithms);
  if(nAlgorithms.match(/^([1-9]|10)$/)){
    $('#spanErrorAlgorithms').css('display', 'none');
    $('#nAlgorithms').css('color','inherit');
    console.log('acepto...');
    $('#insertAlgorithm').show();
  }else{
    console.log('no acepto');
    $('#nAlgorithms').css('color','#FF0000');
    $('#spanErrorAlgorithms').css('display', 'inherit');
    $('#insertAlgorithm').hide();
  }
}