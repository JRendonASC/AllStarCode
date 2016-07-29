var x=50;
var y=50;
function setup(){
	createCanvas(600,600);
	background(0);
	rect(0,100,450,50);
	rect(400,200,200,50);
	rect(0,300,450,50);
	rect(400,400,200,50);
	fill(255,0,0);
	rect(500,500,75,75);
}

function draw(){
	if (keyIsDown(LEFT_ARROW))
		x-=5;
	if (keyIsDown(RIGHT_ARROW))
		x+=5;
	if (keyIsDown(UP_ARROW))
		y-=5;
	if (keyIsDown(DOWN_ARROW))
		y+=5;
	fill(0,0,255);
	ellipse(x,y,40,40);
}
