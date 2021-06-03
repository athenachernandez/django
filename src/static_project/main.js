$(document).ready(function() {
    console.log('hello world')
    $('#modal-btn').click(function() {
        $('.ui.modal')
        .modal('show')
        ;
    })
    $('.ui.dropdown').dropdown()
})