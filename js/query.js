$.get("data.json", function (data) {

  let items = data.map((item, idx) => {
    return {
      ...item,
      id: idx + 1,
      Judul: '<a href="' + item.Link + '" target="_blank">' + item.Judul + '</a>',
    };
  });

  $(document).ready(function () {
    $('#scrap').DataTable({
      data: items,
      columns: [
        { data: 'id' },
        { data: 'Judul' },
        { data: 'Kategori' },
        { data: 'Publish' },
        { data: 'Scraping' },
        { data: 'Link', visible: false }
      ],
      responsive: true
    });
  });
});
