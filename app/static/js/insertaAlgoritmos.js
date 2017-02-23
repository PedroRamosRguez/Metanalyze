/*Script para la introduccion de los nombres de algoritmos que el usuario quiera darle
Además, una vez se inserta, y se le da al boton aparecerá el input para asignar fichero y 
un botón para enviarlo a la base de datos o json pertinente...*/

insertaAlgoritmo = () =>{
  let valor = document.getElementById('algoritmo').value;
  //variable para que cuente la longitud del input introducido
  let contador= document.getElementById('algoritmo').value.length;
  console.log(contador)
  if(contador !== 0){
    $('#introduceAlgoritmo').show()
    $('#ficheroPruebas').show();
    document.getElementById('introduceAlgoritmo').innerHTML = 'Introducir algoritmo: ' + valor;
  }else{
    $('#introduceAlgoritmo').hide();
    $('#ficheroPruebas').hide();
  }
  return valor
}