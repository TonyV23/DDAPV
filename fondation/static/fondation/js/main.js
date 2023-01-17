// GetCommune by province_id
$(function () {
  $("#id_nom_de_la_province").on("change", function () {
    id_nom_de_la_province = $(this).val();
    //alert(id_nom_de_la_province);
    $.get(
      "/refugees/getCommunes",
      {
        id_nom_de_la_province: id_nom_de_la_province,
      },
      function (data, textStatus, jqXHR) {
        $("#id_nom_de_la_commune").html(data);
      }
    );
  });
});
