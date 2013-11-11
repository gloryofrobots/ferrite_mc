 SeriesTable = function(){
    this.init = function(table_id,options) {
        this.options = options;
        this.table_id = table_id;
        this.table = $('#'+this.table_id).dataTable(this.options);
    }

    this.sort = function(columns) {
        this.table.fnSort( columns );
    }

    this.draw = function() {
        this.table.fnDraw();
    }
}

gSeriesTable = new SeriesTable();


function filter_by_type(type) {
    reset_filter();
    $.fn.dataTableExt.afnFiltering.push(
        function( oSettings, aData, iDataIndex ) {

            var type_column = aData[1].toLowerCase();
            //alert(type + "--" + type_column + "--"+ aData[0]);
            if(type == type_column) {

                //alert("ok");
                return true;
            }
            return false;
        }
    );
    gSeriesTable.draw();
}

function reset_filter() {
      while( $.fn.dataTableExt.afnFiltering.length > 0) {
        $.fn.dataTableExt.afnFiltering.pop();
    }
}

function reset_filter_and_draw() {
    reset_filter();
    gSeriesTable.draw();
}