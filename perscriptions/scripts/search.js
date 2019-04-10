$(document).ready(function () {


  $.extend( $.fn.dataTableExt.oStdClasses, {
      "sFilterInput": "form-control",
      "sLengthSelect": "form-control"
  });
  $('table.datatable').DataTable(
  		{
  			'aoColumnDefs': [{
  								'bSortable': false,
  								'aTargets': ['nosort']
  							}],
        "order": [[ 1, "asc" ]]
  		});
})
