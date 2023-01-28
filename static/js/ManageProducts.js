$("#checkAll").change(function () {
    $("input:checkbox").prop('checked', $(this).prop("checked"));
});


const bt = document.querySelector('#delete_btn');
        bt.addEventListener('click', (event) => {
            if(confirm("Are you sure you want to delete ?")){
            let checkboxes = document.querySelectorAll('input[name="checkboxRow[]"]:checked');
            let output = [];
            var csrf = $('input[name=csrfmiddlewaretoken]').val();
            checkboxes.forEach((checkbox) => {
                output.push(checkbox.value);
            });
            if(output.length===0){
                alert("pleace select products by checked you want to delete !!");
            }else{
                console.log(output);
                $.ajax({
                    url:'.',
                    method:"POST",
                    data:{output, csrfmiddlewaretoken:csrf },
                    success:function(response){
                        for (var i = 0; i < output.length; i++) {
                            $('tr#'+output[i]+'').css('background-color','#ccc');
                            $('tr#'+output[i]+'').fadeOut('slow');
                        }
                    }

                })
            }
            
}});    
