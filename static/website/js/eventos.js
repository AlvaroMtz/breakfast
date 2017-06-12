var keys={
  UP: 38,
  DOWN: 40,
  LEFT: 37,
  RIGHT: 39
};

document.addEventListener("keyup", keyboardDraw);
var grid = document.getElementById("drawing_area");
var sheet = grid.getContext("2d");
var x = 150;
var y = 150;


function drawLine(color, x1, y1, x2, y2, canvas)
{
    canvas.beginPath();
    canvas.strokeStyle = color;
    canvas.lineWidth = 2;
    canvas.moveTo(x1, y1);
    canvas.lineTo(x2, y2);
    canvas.stroke();
    canvas.closePath();
}

function keyboardDraw(event)
{
  var color = "#AFA";
  var move = 10;

  switch (event.keyCode) {
    case keys.DOWN:
      drawLine(color, x, y, x, y + move, sheet);
      y = y + move;
      break;
    case keys.UP:
      drawLine(color, x, y, x, y - move, sheet);
      y = y - move;
      break;
    case keys.LEFT:
      drawLine(color, x, y, x - move, y, sheet);
      x = x - move;
      break;
    case keys.RIGHT:
      drawLine(color, x, y, x + move, y, sheet);
      x = x + move;
      break;

  }

}
