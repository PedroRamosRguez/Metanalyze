/*Script que oculta algunos elementos de la web cuando se carga...*/
document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('select');
});

 $(document).ready(() =>{
 	/*Función de Jquery de materialize para la carga del multiselect*/
 	// $('select').material_select();
	 $('select').formSelect();
 	/* Función de Jquery para la barra de navegación en pantallas pequeñas*/
	  $('.button-collapse').sidenav();
    $('#introduceAlgoritmo').hide();
    $('#spanErrorInstancia').css('display', 'none');
    $('#spanErrorAlgorithms').css('display', 'none');
    $('#introduceInstancia').hide();
		$('#insertAlgorithm').hide();
		$('#algorithmConfiguration').hide();
		//$('#selectMetric').hide();
		$('#selectBound').hide();
		// $('#xAxisChart').hide();
  })


