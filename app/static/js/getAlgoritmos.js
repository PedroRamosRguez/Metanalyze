/*Script para obtener los algoritmos que se han introducido por el usuario*/
//crear un json con el que llama a obtener el nombre de los algoritmos (getAlgorithmName) y añadirlo al json que
//devuelve el configureAlgorithm()
const algoritmos = [];
$('#introduceAlgorithm').click(() =>{
  let alg = configureAlgorithm();
  algoritmos.push(alg);
  console.log(algoritmos);
  //$('#introduceAlgorithm').hide();
  //$('#testFile').hide();
});

getAlgoritmos= () =>{
  return algoritmos;
}