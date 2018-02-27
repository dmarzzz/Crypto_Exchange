//This file contains the JavaScript for dashboard.html

var tableTimer;

$(document).ready(function(){

	//Create HTML table
	var columns = 4;
	var rows = 16;

	for(let i = 0; i < rows; i++){
		var rowNode = document.createElement("TR");
		for(let j = 0; j < columns; j++){
			var dataCellNode = document.createElement("TD");
			var textNode = document.createTextNode("Test");
			dataCellNode.appendChild(textNode);
			rowNode.appendChild(dataCellNode);
		}
		document.getElementById("bid_table").appendChild(rowNode);
	}


	//Generate data
	var coins = ["BTC", "ETH", "LTC", "XRP", "NEO"];
	var orderLimit = 1000;
	var orders = [];
	for(let i = 0; i < orderLimit; i++){
		var coinIndex = Math.floor(Math.random() * coins.length);
		orders.push({
			coin1: coins[coinIndex],
			amount1: Math.floor(Math.random() * 100),
			coin2: coins[coins.length - 1 - coinIndex],
			amount2: Math.floor(Math.random() * 100)
		});
		//console.log(orders[orders.length - 1]);
	}


	var currentIndex = 0;
	var shiftBy = 4;
	var secondsBetweenUpdates = 2;

	//This is the function that's called every x seconds to update the table
	var updateTable = function(){
		var currentRow = $("tr").first();
		for(let i = 0; i < rows; i++){

			var currentCell = currentRow.children().first();

			currentCell.text(orders[currentIndex + i].coin1);
			currentCell = currentCell.next();
			currentCell.text(orders[currentIndex + i].amount1);
			currentCell = currentCell.next();
			currentCell.text(orders[currentIndex + i].coin2);
			currentCell = currentCell.next();
			currentCell.text(orders[currentIndex + i].amount2);

			currentRow = currentRow.next();
		}
		currentIndex += shiftBy;
		console.log(currentIndex);
		//console.log(currentIndex);
	}

	//Call updateTable() every secondsBetweenUpdates seconds
	tableTimer = window.setInterval(updateTable, secondsBetweenUpdates * 1000);


	//Sample graph to build off of
	TESTER = document.getElementById('graph');
	Plotly.plot(TESTER, [{
		x: [1, 2, 3, 4, 5],
		y: [1, 2, 4, 8, 16]
	}], {
		margin: {
		t: 0
	}});

}); 	//end of document.ready

var getOrderBook = function(){
	$.get("/dashboard/test", function(response){
		console.log(response);
	});
}

var pauseData = function(){
	clearInterval(tableTimer);
}


