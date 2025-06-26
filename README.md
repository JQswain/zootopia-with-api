# zootopia-with-api
## About:
An experiment in exploring html generation from online resources, in conjunction with APIs. currently only using data from API ninjas animlas api.
It allows users to enter an animal of choice and then seraches for all possible animals that match the search and puts them into a template html file to be displayed in the browser.
It is for everyone wishing to play around withb combining APIs, HTML, a tiny bit of CSS and Python.

## Installation:
To install simply clone the repository and apply for a free API key from 'https://api-ninjas.com/', and add it to your own .env file. there are a couple of required libraries, you can simply put 'pip install' these in the terminal to access these libraries.
They are included in the requirements.txt file in the repositiory 

## Usage:
At the moment the interface is fairly limited and allows for generation of whatver animal you wish to find, if your search input is not availble through the API it responds by generating an error message into the html file.
for example if searching for 'fish' it will show all entries relating to fish, but if you type in an integer '13425276' it will only be able to respond with the error message.

## Contribution:
Contribution, especially in the area of CSS, is encouraged but please make a branch in which to experiment, and feel free to make a pull request if you find something interesting you wuld like to share!

