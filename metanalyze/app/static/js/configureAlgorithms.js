/*Script para la introduccion de los nombres de algoritmos que el usuario quiera darle
Además, una vez se inserta, y se le da al boton aparecerá el input para asignar fichero y 
un botón para enviarlo a la base de datos o json pertinente...*/

configureAlgorithm = () =>{
  let valor = document.getElementById('idAlgorithm').value;
  //variable para que cuente la longitud del input introducido
  let contador= document.getElementById('idAlgorithm').value.length;
  //console.log(contador);
  if(contador !== 0){
    $('#introduceAlgorithm').show();
    $('#testFile').show();
    document.getElementById('introduceAlgorithm').innerHTML = 'Introducir algoritmo: ' + valor;
  }else{
    //$('#introduceAlgorithm').hide();
    $('#testFile').hide();
    $('#introduceAlgorithm').hide();
  }  
  return valor;
}