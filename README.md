# BSL Practice 
### Overview
This is a project I have been making to help those learning BSL to practice efficiently. All the words used on the page come from British Sign UK's introduction to BSL course. I also wanted to do this so I could relearn HTML and explore Javascript and CSS as I had never used them before this.  
### Features
Light and Dark Mode: Offering 2 different modes allows the user to choose a mode which benefits them based on their surroundings and preferences. The dark mode can also help save battery on old OLED screens as it consumes less power, it also allows for more efficient practice before bed as it emits less blue light which can negatively effect the eyes.  
Camera: The camera allows you to easily see what you are signing to check if you are correct when you compare it to the video links in BSL dictionary.  
Links to BSL Dictionary: All the random word generators have links to the page in BSL dictionary which is the largest online collection of BSL words.  
Timed Words: This is a feature that automatically gets you a new word every 7 seconds. I created this after testing the new word button and not liking that I had to lean over to my phone to press the button every time I wanted a new word to appear on my screen.
### The Coding
FOr this I used the light WSGI web application framework Flask 3.1( https://flask.palletsprojects.com/en/stable/ ) and python 3.11.9 to create the server side. The I used bootstrap to add visuals, all the pages are coded in HTML with CSS for the styling and Javascript for the interactivity. I used docker files and microsoft azure to turn it into an actual webpage that could be accessed from any device. It can be ran on any sized device but the visuals were specifically made for a computer/laptop or phone.
### In the Future
In the future there is a lot oif thing I would love to do to improve this website, these include:  
Test feature:  
A simple feature that displays a video of a sign and the user has to enter what they think it is and it checks to se if you know what it is or not.  
Finger Spelling Game:  
A simple game where it shows you a word composed of finger spelling signs, then you must enter te word and if it's correct you get a point. 
### Visit Here

You can visit at: https://zoeprojects.jollyriver-24aaeb86.uksouth.azurecontainerapps.io/about  
It may take a few seconds to load the when you first open it as it is contacting the server to collect all the information but afterwards should run smoothly.

### Credits and Acknowledgments   
##### Credits 
Formatting of the Page - Bootstrap  
The letters for the finger spelling game come from wikipedia and are licenced under the creative commons  Attribution-Share Alike 3.0 unported licence ( https://creativecommons.org/licenses/by-sa/3.0/deed.en )
##### Acknowledgments
Thank you to Blueboxes for help on this project and introducing me to tools like Bootstrap as wll as teaching me the basics of javascript so I could add interactively. Also, I want to thank my teachers for first introducing me to my first language Python which makes up the server end of this project.