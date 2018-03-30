console.log("So far so good");

$(document).ready(function(){

	for(let i = 0; i < 3; i++){
		var comment_html = '';
		comment_html += '<div class = "comment_container"><div class = "vote_container">';
		comment_html += '<div class = "vote_count_container">166&nbsp;</div><div class = "vote_buttons_container">';
		comment_html += '<input type = "button" class = "vote_button" value = "Upvote">';
		comment_html += '<input type = "button" class = "vote_button" value = "Downvote">';
		comment_html += '</div></div><div class = "comment_text_container">This is random garbage text. It doesn\'t have any value or purpose; it exists solely as a placeholder.</div></div>';
		document.body.innerHTML += comment_html;
	}



});