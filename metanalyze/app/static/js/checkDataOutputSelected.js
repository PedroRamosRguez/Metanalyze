$('input[name=dataOutput]').change( (e) => {
	if($('input[name=dataOutput]:checked').next().text().trim() === 'Plot'){
		$('#xAxisChart').show();
	}else if($('input[name=dataOutput]:checked').next().text().trim() === 'Table and Plot'){
		$('#xAxisChart').show();
	}else{
		$('#xAxisChart').hide();
	}
})
