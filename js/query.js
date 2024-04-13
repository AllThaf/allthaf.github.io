// File: query.js
$.get("data.json", function (data) {

  // Membuat array dari 'data'
  let items = data.map((item, idx) => {
    return {
      ...item,
      id: idx + 1,
      Judul: '<a href="' + item.Link + '" target="_blank">' + item.Judul + '</a>',
    };
  });

  // Syntax yang hanya akan apabila DOM siap untuk di eksekusi
  $(document).ready(function () {
    // Display ke headline HTML dengan id scrap
    $('#scrap').DataTable({
      data: items,
      // Isi dari tabel
      columns: [
        { data: 'id' },
        { data: 'Judul' },
        { data: 'Kategori' },
        { data: 'Publish' },
        { data: 'Scraping' },
        { data: 'Link', visible: false }
      ],
      // Agar tabel mobile friendly
      responsive: true
    });
  });
});
