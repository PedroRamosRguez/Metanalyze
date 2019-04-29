/*Script para mostrar y ocultar la elección del límite a elegir por el usuario (mínimo,media,máximo). */

$('#metric').change(() => {
  if($('#metric').val().length > 0){
	//console.log('hay algo seleccionado')
	 	$('#selectBound').show();
  }else{
    $('#selectBound').hide();
	//console.log('no hay algo seleccionado')
  }
})
