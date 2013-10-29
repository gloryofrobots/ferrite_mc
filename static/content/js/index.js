
function show_article(article_id){
	jQuery.post('/articles/show',{'id':article_id,code:Math.floor(Math.random()*(99999999+1))}
										,function(html){ 
											$("#place_for_article").html(html);
										},"text");

}


 $(document).ready(function(){
		
		if($("#lightBox a[rel^='prettyPhoto']").prettyPhoto)	
				$("#lightBox a[rel^='prettyPhoto']").prettyPhoto({
				theme: 'light_rounded'
		});
		/*theme: 'light_rounded'
		$(".galleryclick").click(function(){
				//'#big_photo'
				var $img=$(this).parent().find('img');
				var images=[];
				var descriptions=[];
				var titles=[];
				$img.each(function(key,i){ images.push(i.src); descriptions.push(i.alt); titles.push('');  })
				images.reverse();   descriptions.reverse(); titles.reverse();     
				$.prettyPhoto.open(images,titles,descriptions);
				});
				*/
		$(".gallery img").click(function(event){
		
		//'#big_photo'
       	var i=$(this);
		var images=[];
       	var descriptions=[];
      	var titles=[];
		images.push(i.attr('src')); descriptions.push(i.attr('alt')); titles.push('');
	      	  // images.reverse();   descriptions.reverse(); titles.reverse();     
		$.prettyPhoto.open(images,titles,descriptions);
		});
				
	});
	