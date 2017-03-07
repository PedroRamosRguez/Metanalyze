/*Script para comprobar que el numero de instancias es de 1-99 y muestra un mensaje tipo span 
mostrando un error...*/

/*compruebaInstancia = () => {
  let instancia = document.getElementById('nInstancia').value;
  console.log(instancia);
  if(instancia.match(/^[1-9][0-9]{0,1}$/)){
    $('#spanErrorInstancia').css('display', 'none');
    $('#nInstancia').css('color','inherit');
    console.log('acepto...');
    $('#introduceInstancia').show();
  }else{
    console.log('no acepto');
    $('#nInstancia').css('color','#FF0000');
    $('#spanErrorInstancia').css('display', 'inherit');
    $('#introduceInstancia').hide();
  }
}
*/
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