const algoritmos = []
  $("#introduceAlgoritmo").click(() =>{
    let alg = insertaAlgoritmo()
    algoritmos.push(alg)
    console.log(algoritmos)
    $("#introduceAlgoritmo").hide();
    $("#ficheroPruebas").hide();
  });
 getAlgoritmos= () =>{
  return algoritmos;
}