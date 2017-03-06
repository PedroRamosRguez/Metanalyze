/*Script para obtener los algoritmos que se han introducido por el usuario*/
const algoritmos = [];
$('#introduceAlgorithm').click(() =>{
  let alg = configureAlgorithm();
  algoritmos.push(alg);
  console.log(algoritmos);
  $('#introduceAlgorithm').hide();
  $('#testFile').hide();
});

getAlgoritmos= () =>{
  return algoritmos;
}