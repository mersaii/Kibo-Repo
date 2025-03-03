const questions = [
    {
        "category": "General Knowledge",
        "type": "multiple",
        "difficulty": "medium",
        "question": "What is the last letter of the Greek alphabet?",
        "correct_answer": "Omega",
        "incorrect_answers": [
            "Mu",
            "Epsilon",
            "Kappa"
        ]
    },
    {
        "category": "General Knowledge",
        "type": "multiple",
        "difficulty": "easy",
        "question": "According to Sherlock Holmes, &quot;If you eliminate the impossible, whatever remains, however improbable, must be the...&quot;",
        "correct_answer": "Truth",
        "incorrect_answers": [
            "Answer",
            "Cause",
            "Source"
        ]
    },
    {
        "category": "General Knowledge",
        "type": "multiple",
        "difficulty": "medium",
        "question": "What was the original name of the search engine &quot;Google&quot;?",
        "correct_answer": "BackRub",
        "incorrect_answers": [
            "CatMassage",
            "SearchPro",
            "Netscape Navigator"
        ]
    },
    {
        "category": "General Knowledge",
        "type": "multiple",
        "difficulty": "easy",
        "question": "Which country, not including Japan, has the most people of japanese decent?",
        "correct_answer": "Brazil",
        "incorrect_answers": [
            "China",
            "South Korea",
            "United States of America"
        ]
    },
    {
        "category": "General Knowledge",
        "type": "multiple",
        "difficulty": "hard",
        "question": "How many notes are there on a standard grand piano?",
        "correct_answer": "88",
        "incorrect_answers": [
            "98",
            "108",
            "78"
        ]
    },
    {
        "category": "General Knowledge",
        "type": "multiple",
        "difficulty": "hard",
        "question": "In the MMO RPG &quot;Realm of the Mad God&quot;, what dungeon is widely considered to be the most difficult?",
        "correct_answer": "The Shatter&#039;s",
        "incorrect_answers": [
            "Snake Pit",
            "The Tomb of the Acient&#039;s",
            "The Puppet Master&#039;s Theater"
        ]
    }
]

// your game code goes here

document.addEventListener('DOMContentLoaded', function() {

    startButton.addEventListener('click', function() {
        const playerName = playerNameInput.value.trim();
        if (playerName !== '') {
            welcomeScreen.style.display = 'none';
            gameScreen.style.display = 'block';
            greetingMessage.textContent = `Hello, ${playerName}!`;

            // Display the first question with answer buttons
            displayQuestion(currentQuestionIndex);
        } else {
            alert('Please enter your name before starting the game.');
        }
    });
});


const questionContainer = document.getElementById('question-container');
const answerButtonsContainer = document.getElementById('answer-buttons-container');
const showAnswerButton = document.getElementById('showAnswerButton');
const correctCounterElement = document.getElementById('correctCounter');
const inCorrectCounterElement = document.getElementById('inCorrectCounter')
const goodbyeScreen = document.getElementById('goodbye-screen');
const playAgainButton = document.getElementById('play-again-button');

const welcomeScreen = document.getElementById('welcome-screen');
const gameScreen = document.getElementById('game-screen');
const playerNameInput = document.getElementById('player-name');
const startButton = document.getElementById('start-button');
const greetingMessage = document.getElementById('greeting-message');

let correctCounter = 0;
let inCorrectCounter = 0;
let currentQuestionIndex = 0;

function displayQuestion(index) {
    if (index < questions.length) {
        currentQuestion = questions[index];

        // Create HTML elements for the question
        const questionElement = document.createElement('p');
        questionElement.textContent = currentQuestion.question;

        // Create HTML elements for answer buttons
        const answerButtons = [currentQuestion.correct_answer];
        for(let ans of currentQuestion.incorrect_answers){
            answerButtons.push(ans)}
        answerButtons.sort(() => Math.random() - 0.5); // Shuffle the answer buttons

        const answerButtonsElements = []
        answerButtons.forEach ((answer) => {
            const button = document.createElement('button'); // create each button
            button.textContent = answer;

            answerButtonsElements.push(button);


            button.addEventListener('click', function() {
                checkAnswer(answer, currentQuestion.correct_answer);
            });

            return button;
            
        })

        // Append question and answer buttons to the respective containers
        questionContainer.innerHTML = '';
        questionContainer.appendChild(questionElement);

        answerButtonsContainer.innerHTML = '';
        answerButtonsElements.forEach(button => {
            answerButtonsContainer.appendChild(button);

        correctCounterElement.textContent = 'Correct Answers: ' + correctCounter;
        inCorrectCounterElement.textContent = 'Incorrect Answers: ' + inCorrectCounter;

        });

    } else {
        // No more questions, finish the game show and handle play again button 
        alert('Game Over! You answered ' + correctCounter + ' questions correctly.');
        gameScreen.style.display = 'none';
        goodbyeScreen.style.display = "block";
        // correctCounterElement.textContent = 'Correct Answers: ' + correctCounter;
        // inCorrectCounterElement.textContent = 'Incorrect Answers: ' + inCorrectCounter;
        // playAgainButton.style.display = "block"
        // if (playAgainButton){
            playAgainButton.addEventListener('click', function() {
                // Reset any other game-related state or variables 
                welcomeScreen.style.display = 'block';
                gameScreen.style.display = 'none';
                goodbyeScreen.style.display = 'none';
                playerNameInput.value = '';
                correctCounter = 0;
                inCorrectCounter = 0;
                

                currentQuestionIndex = 0
                // Display the first question with answer buttons
                displayQuestion(currentQuestionIndex);
            });
        // }
    }
}

// Event listener for the "Show Correct Answer" button
showAnswerButton.addEventListener('click', function() {
    alert('Correct Answer: ' + currentQuestion.correct_answer);
    });

function checkAnswer(selectedAnswer, correctAnswer) {
    if (selectedAnswer === correctAnswer) {
        // Increment correct answer  and update display
        correctCounter++;
        alert('Correct!');

    } else {
        inCorrectCounter++;
        alert('Incorrect!');
    }

    // Update the display
    // correctAnswersDisplay.textContent = correctAnswers;
    // incorrectAnswersDisplay.textContent = incorrectAnswers;

    // Display the next question or finish the game
    currentQuestionIndex++;
    displayQuestion(currentQuestionIndex);
}


// const correctAnswersDisplay = document.getElementById('correct-answers');
// const incorrectAnswersDisplay = document.getElementById('incorrect-answers');

