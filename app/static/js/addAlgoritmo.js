/*Script que añade el algoritmo que se haya insertado anteriormente y gestiona la insterfaz.*/

//const algoritmos=[]
$("#introduceAlgoritmo").click(() =>{
  $('#introduceAlgoritmo').prop("disabled")
  //$("#ficheroPruebas").css("display", "inherit");
  let algoritmoIntroducido = insertaAlgoritmo()
  //$("#algoritmo").val('')
  //$("#introducealgoritmo").css("display", "none");
  //algoritmos.push(algoritmoIntroducido)
  //console.log(algoritmoIntroducido)
  //console.log('introducido el algoritmo...')
  alert('algoritmo introducido');
  $("#introduceAlgoritmo").hide();
  $("#ficheroPruebas").hide();
  //return(algoritmoIntroducido);
}); 
