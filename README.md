# Bookmarks Parsing Python Script

Ummmmmm. I started using ur code but got rid of alot of it lol. Python for life 😎

## Table OF Contents

<!-- TOC -->

- [Bookmarks Parsing Python Script](#bookmarks-parsing-python-script)
  - [Table OF Contents](#table-of-contents)
  - [What Each File Is...](#what-each-file-is)
- [CSV to Web](#csv-to-web)
  - [Chosen API's / extra code](#chosen-apis--extra-code)
  - [Color Theory](#color-theory)
- [Machine Learning Model](#machine-learning-model)

<!-- /TOC -->

## What Each File Is...

- main.py is the main python file, once the whole project is done, this should be the only nessecary file.

- all the other files ending in .py will be used in that main.py file, if one component their names may give hints to what needs debugging.

- the bookmarks.csv is the bookmarks.html cleaned and turned to csv in one.
- the night_tab.csv is the night_tab.json cleaned and turned to csv in one.

This README.md is so people like me and you can remember what the fuck this whole thing means when we move onto another project and forget about all of this.

**Unessesary Added Complexities**
I decided I will be using an ai model to not only categorise the bookmarks and give appropriate quick suggestions but also to help generate favicons. I may also need a icon library such as fontawesome to use in combination.

My only worry currently is that it doesnt fit everything well enough, like youtube links will probably all come under visual / entertainment even if their content can be drastically different depending on the video

# CSV to Web

Turning the csv generated from the process before (firefox bookmarks to csv and nighttab bookmarks to csv) and using those combined csv files as data to flow into a webpage as their bookmarks under their categories.

For the website I want a focus to be on integrating the python script into it and being able to edit how folders look and interact. With a focus on the data handling and how users can import more data if they wish and formatting data themselves as they please.

## Chosen API's / extra code

- Read CSV data with JavaScript/TypeScript and store in an array/object
- Create HTML elements dynamically for each bookmark with a loop
- Use a third-party API like RealFaviconGenerator to generate a favicon for each bookmark
- https://github.com/RealFaviconGenerator/rfg-api
- https://realfavicongenerator.net/

---

- Use a consistent color scheme and font
- CSS transitions and hover effects

## Color Theory

![](gen_colorsheme.png)
**(Generated From Coolors)**

    If the background color is #0000FF (blue), you could use #FFFFFF (white) for h1 and #1E90FF (dodger blue) for h3. For the background color, you could use #F5DEB3 (wheat), which provides a good contrast with blue and makes the text easy to read.

    If the background color is #228B22 (forest green), you could use #FFFFFF (white) for h1 and #1E90FF (dodger blue) for h3. For the background color, you could use #F5DEB3 (wheat), which provides a good contrast with green and makes the text easy to read.

    If the background color is #800080 (purple), you could use #FFFFFF (white) for h1 and #1E90FF (dodger blue) for h3. For the background color, you could use #D8BFD8 (thistle), which provides a good contrast with purple and makes the text easy to read.

    If the background color is #1E90FF (dodger blue), you could use #FFFFFF (white) for h1 and #0000FF (blue) for h3. For the background color, you could use #F5DEB3 (wheat), which provides a good contrast with blue and makes the text easy to read.

    If the background color is #008000 (green), you could use #FFFFFF (white) for h1 and #1E90FF (dodger blue) for h3. For the background color, you could use #F5DEB3 (wheat), which provides a good contrast with green and makes the text easy to read.

    If the background color is #D8BFD8 (thistle), you could use #000000 (black) for h1 and #800080 (purple) for h3. For the background color, you could use #FFFFFF (white), which provides a good contrast with thistle and makes the text easy to read.

    If the background color is #006400 (dark green), you could use #FFFFFF (white) for h1 and #1E90FF (dodger blue) for h3. For the background color, you could use #F5DEB3 (wheat), which provides a good contrast with dark green and makes the text easy to read.

    If the background color is #F5DEB3 (wheat), you could use #000000 (black) for h1 and #800080 (purple) for h3. For the background color, you could use #FFFFFF (white), which provides a good contrast with wheat and makes the text easy to read.

    If the background color is #FFFF00 (yellow), you could use #000000 (black) for h1 and #800080 (purple) for h3. For the background color, you could use #006400 (dark green), which provides a good contrast with yellow and makes the text easy to read.

    If the background color is #FFD700 (gold), you could use #000000 (black) for h1 and #800080 (purple) for h3. For the background color, you could use #F5DEB3 (wheat), which provides a good contrast with gold and makes the text easy to read.

**(Generated From ChatGPT)**

# Machine Learning Model

ummmm.
