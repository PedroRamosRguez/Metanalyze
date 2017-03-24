/*Script para mostrar y ocultar las metricas a elegir por el usuario en caso de que seleccione o no
el limite a calcular (minimo,maximo y media). */
$('#bound').change(() => {
  if($('#bound').val().length > 0){
	//console.log('hay algo seleccionado')
	 	$('#selectMetric').show();
  }else{
    $('#selectMetric').hide();
	//console.log('no hay algo seleccionado')
  }
})
  

