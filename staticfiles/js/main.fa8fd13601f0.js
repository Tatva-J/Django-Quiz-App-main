// console.log("Hello world");

// var checkBtn = document.getElementById('check');
var answerLabel = document.getElementById("answerLabel");
var nextBtn = document.getElementById("next-btn");
var finishBtn = document.getElementById("finish-btn");
var showResultBtn = document.getElementById("show-result-btn");
var dummyBtn = document.getElementById("dummy");

if (nextBtn) {
  if (nextBtn.length > 0) {
    finishBtn.setAttribute("hidden", true);
    showResultBtn.setAttribute("hidden", true);
  } else {
    finishBtn.setAttribute("hidden", false);
    showResultBtn.setAttribute("hidden", false);
  }
}
function displayHintValue() {
  result_div1.innerHTML = `
				<div class="h5 mb-3"><b>Hint1 for the first question is ${hint11.value}</b></div>
				`;
}
function displayHint1Value() {
  result_div2.innerHTML = `
				<div class="h5 mb-3"><b>Hint2 for the first question is ${hint22.value}</b></div>
				`;
}
function displayRadioValue() {
  var ele = document.getElementsByName("option");
  for (i = 0; i < ele.length; i++) {
    if (ele[i].checked) {
      checked_val = ele[i].value;
      if (checked_val == answerLabel.value) {
        console.log("Correct");
        document.getElementById("check").disabled = true;
        document.getElementById("option_one").disabled = true;
        document.getElementById("option_two").disabled = true;
        document.getElementById("option_three").disabled = true;
        document.getElementById("option_four").disabled = true;
        result_div.innerHTML = `
				<div class="h5 mb-3"><b>Correct</b></div>
				`;
      } else {
        console.log("Wrong");
        document.getElementById("check").disabled = true;
        document.getElementById("option_one").disabled = true;
        document.getElementById("option_two").disabled = true;
        document.getElementById("option_three").disabled = true;
        document.getElementById("option_four").disabled = true;
        result_div.innerHTML = `
				<div class="h5 mb-3"><b>Wrong, Correct answer is ${answerLabel.value}</b></div>
				`;
      }
    }
  }
}

var totalScore = document.getElementById("totalScore"); //id of the total score text field
var userScore = 0;
var checkBtn = document.getElementById("check"); //Id of the check button
if (checkBtn) {
  checkBtn.addEventListener("click", function () {
    var ele = document.getElementsByName("option");
    for (i = 0; i < ele.length; i++) {
      if (ele[i].checked) {
        checked_val = ele[i].value;
        if (checked_val == answerLabel.value) {
          sessionStorage.getItem('userScore');
          userScore += parseInt(points.value);
          sessionStorage.setItem("userScore", userScore);
          console.log(userScore);
        }
      }
    }
  });
}
var checkBtn1 = document.getElementById("hint"); //Id of the check button
if (checkBtn1) {
  checkBtn1.addEventListener("click", function () {
    console.log("Its Working");
  }
  );
}
if (dummyBtn) {
  dummyBtn.addEventListener("click", function () {
    totalScore.value = sessionStorage.getItem("userScore");
  });
}
