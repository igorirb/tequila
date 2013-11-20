$(document).ready(function () {
	$('#tq-dates-submit').click(function() {
		var start = $('#id_starts_at').val().split("/");
		start = start[2] + start[0] + start[1];
		var end = $('#id_ends_at').val().split("/");
		end = end[2] + end[0] + end[1];
		$('#tq-dates-form').attr('action','/events/' + start + '/' + end + '/');
		if (start != '' && end != '')
			if (parseInt(start) > parseInt(end))
				alert("A data de início deveria ser menor que a de fim.");
			else
				$('#tq-dates-form').submit();
		else
			alert("Insira uma data válida para início e fim do período.");
	});

	$("#id_starts_at").datepicker();
	$("#id_ends_at").datepicker();
});