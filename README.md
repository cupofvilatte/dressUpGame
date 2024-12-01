# Overview

This project is a dress-up game designed to help me learn the basics of game development using Python and PyGame. The goal is to create a simple, interactive experience that allows users to drag and drop clothing items onto a character.

In this game, players can select various clothing items and accessories to dress up a character by dragging and dropping them onto the character. The game supports basic interaction through mouse input, and the visuals are displayed in a graphical interface.

The purpose of this software is to gain experience with PyGame, practice working with graphics and user input, and develop a better understanding of how to structure game projects.

This game is a dress-up game. You simply run the game, and then are able to change the clothing of the character. This game works by dragging and dropping the clothing items into place. Future implementations will have the clothing automatically snap into the precise location. For now, the freedom allows personal input in clothing alignment.

The game works by rendering a background and characters which are locked into place. While running, the game checks for events of mouse clicks. When a mouse is clicked on an item, that item will become the dragged item, and will follow the motion of the mouse. When the mouse is released, the item will remain where it was dropped.

I loved playing dress up games when I was young, so I wanted to experiment with this. One of my goals in this was to make the dress up character modest, as I think children's games should be enjoyed without the risk of objectifying artwork.

[Software Demo Video](https://youtu.be/SbiFeaJykPE)

# Development Environment

I used Visual Studio Code (VSCode) and GitHub to develop this project. I used GitHub and git source control for keeping track of the development. I used VSCode to build the game in Python.

For the images in this game I used Pixelart.com, which is a free site online that allows you to make pixel images. You can use layers, which is how I created clothing that matches the design of the character. You are also able to export images by the entire painting or by layer. I used the Mac built-in photo editor, Preview, to crop images to my need. It's a very simple editor with only basic capabilities, but it was sufficient for this project.

I used Python to build this game, and worked with the module PyGame, which is made for easy game development in Python.
Python is a very popular high-level programming language. PyGame is also a popular module, and can be used to easily render graphics and implement game features.
I also used sys, which allows me to have a runtime and to exit the program effectively.

# Useful Websites

* [PyGame Official Site](https://www.pygame.org/docs/)
* [Royalty Free Music](https://pixabay.com/music/)
* [Pixilart](https://www.pixilart.com)
* [Intro to PyGame YouTube](https://youtu.be/AY9MnQ4x3zk?si=YE5g-WCbOWdWRk_T)

# Future Work

* Add more clothing options and accessories.
* Implement a snapping mechanism to align clothing precisely on the character.
* Create a save option to export the final outfit as an image.
* Add a main menu and customization options like background changes.
* Improve the user interface with buttons and better visual feedback.