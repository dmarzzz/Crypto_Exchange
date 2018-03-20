console.log("So far so good");

$(document).ready(function(){

	for(let i = 0; i < 3; i++){
		document.body.innerHTML += '<div class = "comment_container" style = "width: 100%; height: 10%; border: 1px solid black; box-sizing: border-box; margin: 2% 0 0 0;"><div style = "width: 15%; height: 100%; border: 1px solid blue; display: inline-block;"><div style = "width: 40%; height: 100%; display: inline-block; font-size: 250%;">166&nbsp;</div><div style = "width: 40%; height: 100%; display: inline-block;"><input type = "button" style = "width: 90%; height: 50%;" value = "Upvote"><input type = "button" style = "width: 90%; height: 50%;" value = "Downvote"></div></div><div style = "width: 84%; height: 100%; border: 1px solid red; display: inline-block; vertical-align: top;">This is random garbage text. It doesn\'t have any value or purpose; it exists solely as a placeholder.</div></div>'
	}



});