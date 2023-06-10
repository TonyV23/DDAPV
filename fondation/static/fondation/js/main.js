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

$(function () {
  $("#id_province").on("change", function () {
    id_province = $(this).val();
    //alert(id_province);
    $.get(
      "/distributions/getCommunes",
      {
        id_province: id_province,
      },
      function (data, textStatus, jqXHR) {
        $("#id_commune").html(data);
      }
    );
  });
});

// GetAssistance by type_aide_id
$(function () {
  $("#id_type_aide").on("change", function () {
    id_type_aide = $(this).val();
    //alert(id_type_aide);
    $.get(
      "/donations/getAssistance",
      {
        id_type_aide: id_type_aide,
      },
      function (data, textStatus, jqXHR) {
        $("#id_type_assistance").html(data);
      }
    );
  });
});

// GetAssistance by type_aide_id
$(function () {
  $("#id_type_aide").on("change", function () {
    id_type_aide = $(this).val();
    //alert(id_type_aide);
    $.get(
      "/distributions/getAssistance",
      {
        id_type_aide: id_type_aide,
      },
      function (data, textStatus, jqXHR) {
        $("#id_type_assistance").html(data);
      }
    );
  });
});
