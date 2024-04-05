$(function () {

  $.get('data.json', function (obj) {
    var str = "<table border =1>";
    str += "<tr><td>No</td><td>Judul</td><td>Kategori</td><td>Waktu Publish</td><td>Waktu Scraping</td></tr>";

    $.each(obj, function (n, data) {
      str += "<tr><td>" + (n + 1) + "</td>";
      str += "<td><a href='" + data.Link + "' target ='_blank'>" + data.Judul + "</a></td>";
      str += "<td>" + data.Kategori + "</td>";
      str += "<td>" + data.Publish + "</td>";
      str += "<td>" + data.Scraping + "</td></tr>";

    });

    str += "</table>";
    $("#scrap").html(str);
  });
});