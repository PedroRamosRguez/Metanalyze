$('input[name=dataOutput]').change( (e) => {
	if($('input[name=dataOutput]:checked').val() =='plot'){
		$('#xAxisChart').show();
	}else if($('input[name=dataOutput]:checked').val() =='table-plot'){
		$('#xAxisChart').show();
	}else{
		$('#xAxisChart').hide();
	}
})
