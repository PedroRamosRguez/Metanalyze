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


/*Función que lo muestra el número de instancias que el usuario haya introducido con su input de texto
y lo que hace es que al darle al botó + de añadir instancia, "limpia" de la pantalla la configuración de
la instancia introducida.*/

introduceInstancias = (i) => {
  //funcion de jquery para comprobar que se tiene un array de botones.  
  $(`#btninstancia${i}`).each(() => {

    let input = document.getElementById(`instancia${i}`).value;
    console.log(input);
    console.log('le diii y soy el boton '+ i);
    //cambiar a remove para ver si no borra datos..
    $(`#btninstancia${i}`).css("display","none");
    $(`#instancia${i}`).css("display","none");
  })
}

