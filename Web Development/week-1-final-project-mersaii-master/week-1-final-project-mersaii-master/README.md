# Instructions

---

## 1. Preamble

We will test what you've learned so far by building a Trivia Game. 

![https://phandroid.s3.amazonaws.com/wp-content/uploads/2018/01/hq-trivia-android-screenshot.jpg](https://phandroid.s3.amazonaws.com/wp-content/uploads/2018/01/hq-trivia-android-screenshot.jpg)

## 2. Project Summary

**What do I have to do exactly?**

You will build the Web application of a *trivia*. Your trivia is single-player.

All questions have 4 possible answers, but only one is the correct one.

The main objective of this project is to have a first experience developing Web applications that interact with users through the browser, using HTML, CSS, and JavaScript.

We are providing you with the questions, you can add more if you want but you should use these 6 questions as a minimum.

Please check in the `src` folder, you have `trivia.js` that contains the questions data and this is where you should write your game code. Also, you have `index.html`, where you should write your HTML code and `styles.css` where you should write your CSS styles. 

You can choose the colors and the design of your game. 

## 3. Learning Objectives

- Create an HTML website
- Use CSS to create beautiful UI (User interfaces)
- Learn how to improve your web application usability (UX)
- Code in JS to make your website dynamic, which between questions, add feedback messages to your users, etc

> We will provide you the project skeleton, with all the required files to be able to easily get started
> 

## 4. General Considerations

- The project logic must be fully implemented in JS, HTML, and CSS. In this project, it is **NOT** allowed to use libraries or frameworks, only [vanilla JavaScript](https://www.notion.so/Instructions-a42ccef14af441409e159e29538674ee)
- The goal is to learn, not only to "finish and deliver".
- We want to see you learn what you still do not know. Be transparent so that we can understand your learning process.

## 5. Recommendations

### Prototype

Something that always helps to "make it more tangible" you can draw a prototype **of the entire project on paper and pencil**. 

Drawing is a quick process that allows you to understand how, when, and where things happen; Where exactly should such and such a thing say, what happens if the user does A or B, where should they click, what information exactly do you want to show them, etc. **Devote a maximum of two hours to this before you start coding.**

### Don't procrastinate what you don't know how to do, start there

Don't spend hours discussing the theme of the *trivia* or making logos with the feeling that you are "moving forward". It is natural that you have the impulse to do so, it is your brain asking for its dose of **immediate satisfaction**. Do not be fooled by the "illusion" of progress, **your goal is to learn**. Face what you do not know as soon as possible, it is the only way to achieve it.

### Learn above completing the project

Avoid the temptation to copy and paste code that "works" to complete the project without understanding how or why it works. Always prefer to do little but something that you understand and can explain, rather than much that works halfway and/or that you do not know well how or why it works.

## 6. Project Steps

Total project should take around 3 hours.

### Step 1 (30 minutes)

##### Simple Trivia version

- Display only the first question.
- 1 button to see what is the right answer. (not to actually answer, or buttons to answer, just showing what answer is the correct one)

---

### Step 2 (40 minutes)

##### Add interaction

- List all 4 buttons (with 4 answers) to answer the first question.
- One counter to display how many correct questions I've answered
- When I click one answer and it's correct, the correct answer counter should increase.

---

### Step 3 (60 minutes)

##### Handle more questions

- After I answer a question, I should display to the next question (if there are more questions) or finish the game (if no more remaining questions).

---

### Step 4 (30 minutes)

##### Add a welcome Screen

Add a simple welcome screen with the following elements and features:

- A text box (*input text*) in which the player writes their name.
- There is a "play" or "start" button to answer the questions.
- (While answering questions) Add a section that says: "Hello [the name that was written on the welcome screen]".

---

### Step 5 (20 minutes)

##### Goodbye screen

- A button to play again returns to the initial screen where the name is requested.
- Add a screen at the end for correct and incorrect answers and show a total score at the end.

If you did everything above and have a little more time, decide what else you would like to do to improve your project. You could, for example:

- Add a countdown with a time limit to answer each question. To achieve this, we leave you [a hint of javascript](https://javascript.info/settimeout-setinterval).