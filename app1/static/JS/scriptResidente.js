(function(){
    $("#tabresidentes").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalresidentes").modal("show");
    });

    $("#btnsim").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/residentes_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/residentes_list";
            }
        });
    });
})();
