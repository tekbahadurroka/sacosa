$(document).ready(function() {
    $("#branch").change(function() {
        var branch_id = $(this).val();
        var url = "/get-center/?branch_id=" + branch_id; 
        $.get(url, function(data, status) {
            $("#center").html(data);
        });
    });
});
    
    