(function(){
    $("#tabresponsavel").on("click", ".js-delete", function(){
        let botaoClicado = $(this);
        $("#btnsim").attr("data-id",botaoClicado.attr("data-id"));
        $("#modalresponsavel").modal("show");
    });

    $("#btnsim").on("click",function(){
        let botaoSim = $(this);
        let id = botaoSim.attr("data-id");
        $.ajax({
            url: "/responsavel_delete/" + id,
            method: "GET",
            success: function() {
                window.location.href="/responsavel_list";
            }
        });
    });
})();
