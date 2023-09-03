(function(){
    $("#tabcuidadores").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim-cuidador").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalcuidadores").modal("show");
    });

    $("#btnsim-cuidador").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/cuidadores_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/cuidadores_list";
            }
        });
    });
})();
