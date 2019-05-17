
//carga de los eventos de multiple seleccion de checkbox y la barra de navegacion
document.addEventListener('DOMContentLoaded', function() {
	let select = document.querySelectorAll('select');
	let nav = document.querySelectorAll('.sidenav');
});

 $(document).ready(() =>{
 	/*Función de Jquery de materialize para la carga del multiselect*/
	$('select').formSelect();
	$('.sidenav').sidenav(); 
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


