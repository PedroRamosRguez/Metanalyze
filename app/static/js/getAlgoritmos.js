/*Script para obtener los algoritmos que se han introducido por el usuario*/
const algoritmos = []
  $('#introduceAlgoritmo').click(() =>{
    let alg = insertaAlgoritmo()
    algoritmos.push(alg)
    console.log(algoritmos)
    $('#introduceAlgoritmo').hide();
    $('#ficheroPruebas').hide();
  });
 getAlgoritmos= () =>{
  return algoritmos;
}