<script>
$('.data-dismiss="modal"').click(function(){
  $('video').each(function(){
    $(this).get(0).pause();
  })
});
</script>
