/*Script para introducir el numero de instancias que tiene el problema
 creará un input y un boton por cada n instancia introducida...
 además, también quita la demostración del input de introducir un numero
 de instancias al darle click..

*/
$('#introduceInstancia').click(() => {
  //console.log("di click...");
  let nInstancia = document.getElementById('nInstancia').value;
  //console.log(nInstancia);
  $('#nInstancia').css('display','none');
  $('#introduceInstancia').css('display','none');
  let i=1;
  while(i <= nInstancia){
    let inputInstancias = `<input type="text" name="nInstancia${i}" placeholder="Añadir instancia ${i}" id="instancia${i}"> 
                           <button class="btn-floating waves-effect waves-light grey darken-3" type="button" name="action" id="btninstancia${i}" value=introduceAlgoritmo${i}" onclick="introduceInstancias(${i})">
                             <i class="material-icons right">add</i>
                           </button> `
    $("#addInstancias").append(inputInstancias);
    i+=1;
  }
  i=1;
})


$('#insertAlgorithm').click(() => {
  console.log("di click...");
  let nAlgorithms = document.getElementById('nAlgorithms').value;
  console.log(nAlgorithms);
  $('#nAlgorithms').css('display','none');
  $('#insertAlgorithm').css('display','none');
  let i=1;
  while(i <= nAlgorithms){
    let inputAlgorithms = 
    `<div class="row" >
       <div class="input-field  col s12">
         <input type="text" name="nalgorithm${i}" placeholder="Add Algorithm ${i}" id="algorithm${i}">
         <button class="btn-floating waves-effect waves-light grey darken-3" type="button" name="action" id="btnAlgorithm${i}" value=introduceAlgoritmo${i}" onclick="insertAlgorithms(${i})">
          <i class="material-icons right">add</i>
       </div>
    </div>`
    $("#addAlgorithms").append(inputAlgorithms);

    i+=1;
  }
  i=1;
})