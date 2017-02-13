/*Script para enviar los datos a base de datos o json o array con el nombre de las instancias*/

 function introduceInstancias(i){
  $(`#btninstancia${i}`).each(() => {
    let input = document.getElementById(`instancia${i}`).value;
    console.log(input)
    console.log('le diii y soy el boton '+ i)
    //cambiar a remove para ver si no borra datos..
    $(`#btninstancia${i}`).css("display","none");
    $(`#instancia${i}`).css("display","none");
  })
 }
