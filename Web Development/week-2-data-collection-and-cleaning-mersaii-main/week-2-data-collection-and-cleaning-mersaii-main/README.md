[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/QOGw3bTY)
# Assignment - FIFA '21 Player Ratings

![fifa-assignment](/config/fifa-assignment.jpeg)

## FIFA '21 Player Ratings
The FIFA 21 player rating dataset contains information about the ratings of football players in the FIFA 21 video game. Each player is assigned a rating that reflects their overall skill level in the game. The dataset includes various attributes such as player name, nationality, club, position, and individual attributes like pace, shooting, passing, dribbling, defending, and physicality. These ratings are used to determine player performance and abilities within the game.

Here, you have a very messy and raw dataset of EA Sports' installment of their hit FIFA series - FIFA21, which was scraped from [sofifa.com](https://sofifa.com).

> **NOTE: This is a group assignment with maximum of 3 people in a group**.

### Challenges
One of the challenges of web scraping is unclean data. Different front-end developers and data scientist write the HTML their own way, and that makes the incoming data unpredictable. Your task in this assignment is to clean up this dataset

You'll definitely learn a lot about data cleaning with this dataset.

[![Click to open the project](https://img.shields.io/static/v1?label=Open%20Project&message=FIFA-21%20Player%20Ratings&color=blue)](https://github.com/kiboschool/fifa-21-player-ratings.git)


### TODOs
- Clone the assignment repository using the link above
- Look through the data - `fifa_21_raw_data.csv`
- Read the `hints` below to have an idea of what is required to do with the data.
- Work using the provided notebook in the cloned repo.
    - Push your solution back to Github once completed.
- Put all your charts/graphs in a single file as this will be submitted as part of the assignment on gradescope.
- Once you have covered the hints below, goto assignment on **[Gradescope](https://www.gradescope.com/courses/544001/assignments)**
    - Look for **Week 2 - FIFA '21 Player Ratings**
    - Submit your assignment


### HINTS
- This is a group assignment with **maximum of 3 people in a group**.
- Convert the height and weight columns to numerical forms
- Remove the unnecessary newline characters from all columns that have them.
- Handle duplicate player data from the dataset by dropping duplicate rows, while keeping the first occurrence
- Split the LongName into 2 new coloumns - `first name` and `last name`.
- Handle missing values by filling it with `statistical techniques`.
- Are there outliers in the data? If yes, handle them with any of the techniques you've learnt.
- `Value`, `Wage` and `Release Clause` are string columns. Convert them to numbers. For eg, "M" in value column is Million, so multiply the row values by 1,000,000, etc.
- Convert all currency character to dollar i.e, `$` in column `Value`, `Wage` and `Release Clause`
- Some columns have 'star' characters/icons. Strip those columns of these stars and make the columns numerical
- Go beyond these hints and clean any other inconsistencies you can find.
