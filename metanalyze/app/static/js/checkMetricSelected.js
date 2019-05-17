/*Script para mostrar y ocultar la elección del límite a elegir por el usuario (mínimo,media,máximo). */

$('#metric').change(() => {
  if($('#metric').val().length > 0){
	 	$('#selectBound').show();
  }else{
    $('#selectBound').hide();
  }
})
