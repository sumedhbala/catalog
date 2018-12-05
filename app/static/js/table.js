$.fn.dataTable.ext.buttons.addentry = {
    className: 'add-category',

    action: function(e, dt, node, config) {
        location.href = config.url;
    }
};

$(document).ready(function() {
    $('#categories_table').dataTable({
        searching: false,
        autoWidth: true,
        ordering: false,
        pagingType: "numbers",
        dom: 'Btip',
        buttons: [{
            extend: 'addentry',
            text: 'Add Category',
            url: "/category/add"

        }]
    });
    $('#categories_table_info').parent().removeClass().addClass("mw-100");
    $('#categories_table_paginate').parent().removeClass().addClass("mw-100");
    $('#items_table').dataTable({
        searching: false,
        "autoWidth": true,
        "ordering": false,
        "pagingType": "numbers",
        dom: 'Btip',
        buttons: [{
            extend: 'addentry',
            text: 'Add Items',
            url: "/items/add"
        }]
    });
    $('#items_table_info').parent().removeClass().addClass("mw-100");
    $('#items_table_paginate').parent().removeClass().addClass("mw-100");


    $('#categories_table').on('click', '.view_items', function(e) {
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "/category/items",
            data: {
                category: $(this).val(),
            },
            success: function(items) {
                $("#items_table tbody tr").remove();
                var items_table = $('#items_table').DataTable();
                items_table.clear().draw();
                for (i = 0; i < items.length; i++) {
                    var item_text = items[i].name
                    var item_link = item_text.link(`/category/item?item=${items[i].id}`)
                    items_table.row.add([item_link]);

                }
                items_table.draw();

            },
            error: function(result) {
                alert('error');
            }
        });
    });



});