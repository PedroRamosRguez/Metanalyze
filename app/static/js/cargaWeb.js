/*Script que oculta algunos elementos de la web cuando se carga...*/

 $(document).ready(() =>{
 	/*Función de Jquery de materialize para la carga del multiselect*/
 	$('select').material_select();
    $('#introduceAlgoritmo').hide();
    //$("#ficheroPruebas").css("display", "none");
    $('#ficheroPruebas').hide();
    $('#spanErrorInstancia').css('display', 'none');
    $('#spanErrorAlgorithms').css('display', 'none');
    $('#introduceInstancia').hide();
 	$('#insertAlgorithm').hide();
 	$('#algorithmConfiguration').hide();
  })
/* Función de Jquery para la barra de navegación en pantallas pequeñas*/

$('.button-collapse').sideNav();

