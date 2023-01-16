// GetCommune by province_id
$(function() {
    $('#province_id').on("change", function () {
        province_id = $(this).val();
        //alert(commune_id);
        $.get(
            "/address/getCommunes",
            {
                province_id: province_id,
            },
            function (data, textStatus, jqXHR) {
                $("#id_commune").html(data);
            }
        );
    } );
});
