var x=50;
var y=50;
function setup(){
	createCanvas(600,600);
	}

function draw(){
	background(0);
	fill(255);
	rect(0,100,450,50);
	rect(400,200,200,50);
	rect(0,300,450,50);
	rect(400,400,200,50);
	fill(255,0,0);
	rect(500,500,75,75);
	if (keyIsDown(LEFT_ARROW))
		x-=5;
	if (keyIsDown(RIGHT_ARROW))
		x+=5;
	if (keyIsDown(UP_ARROW))
		y-=5;
	if (keyIsDown(DOWN_ARROW))
		y+=5;
	fill(0,0,255);
	ellipse(x-20,y-20,40,40);
	if ((x>=0 && x<=450) && (y>=100 && y<=150)){
	x=50;
	y=50;
	ellipse(x-20,y-20,40,40);
	}
	if ((x>=400 && x<=600) && (y>=200 && y<=250)){
	x=50;
	y=50;
	ellipse(x-20,y-20,40,40);
	}
	if ((x>=0 && x<=450) && (y>=300 && y<=350)){
	x=50;
	y=50;
	ellipse(x-20,y-20,40,40);
	}
	if ((x>=400 && x<=600) && (y>=400 && y<=450)){
	x=50;
	y=50;
	ellipse(x-20,y-20,40,40);	
	}
	
}