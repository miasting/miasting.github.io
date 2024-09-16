<script>
$('.close-popup').click(function(){
  $('video').each(function(){
    $(this).get(0).pause();
  })
});
</script>
