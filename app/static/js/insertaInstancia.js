/*Script para que al insertar la instancia, haga desaparecer el boton una vez los inserta...*/

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

