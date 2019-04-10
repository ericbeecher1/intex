(function(context) {

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
                  }]
        });
  })

})(DMP_CONTEXT.get());
