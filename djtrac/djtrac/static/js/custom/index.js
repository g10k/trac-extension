$(function () {
    $('[data-toggle="tooltip"]').tooltip();

    $('#id_dt_from').datetimepicker({
         timepicker:false,
         format:'d.m.Y',
         lang:'ru'
    });
    $('#id_dt_to').datetimepicker({
         timepicker:false,
         format:'d.m.Y',
         lang:'ru'
    });
});