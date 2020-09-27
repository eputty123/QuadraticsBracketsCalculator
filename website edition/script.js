function factor() {
  var a = parseInt(document.getElementById("fa").value);
  var b = parseInt(document.getElementById("fb").value);
  var c = parseInt(document.getElementById("fc").value);

  console.log(a);
  console.log(b);
  console.log(c);

  if (a === 1) {} else {
    // Dividing values of b and c by a to exclude the (for example) 2 in 2x^2
    a = a;
    b = (b / a);
    c = (c / a);
  }

  console.log(a);
  console.log(b);
  console.log(c);

  // Adding method of Quadratic Formula
  var quadpos = (-b + Math.sqrt(b * b - 4 * c)) / 2;

  // Subtracting method of Quadratic Formula
  var quadneg = (-b - Math.sqrt(b * b - 4 * c)) / 2;

  console.log(quadpos);
  console.log(quadneg);

  if (a === 1) {
    var factored = "Factored: (x + " + -quadpos + ")(y + " + -quadneg + ")";
  } else {
    var factored = "Factored: " + a + "(x + " + -quadpos + ")(x + " + -quadneg + ")";
  }

  var answer1 = document.getElementById("fanswer1").innerHTML = ("X = " + quadpos);
  var answer2 = document.getElementById("fanswer2").innerHTML = ("X = " + quadneg);
  var answer3 = document.getElementById("fanswer3").innerHTML = (factored);
}

function expand() {
  var a = parseInt(document.getElementById("ea").value);
  var b = parseInt(document.getElementById("eb").value);
  var c = parseInt(document.getElementById("ec").value);

  var expanded = "Expanded: " + a + "x^2 + " + (b + c) * a + "x + " + (b * c) * a;
  var answer1 = document.getElementById("eanswer1").innerHTML = (expanded);
}