This is the final project for 5425 Multimedia Retrival

In this project, we mainly built a website to retrival drugs information base on their pictures!

!First, let me list the package and frame's version:

python                    3.9.16  
flask                     2.2.2            
numpy                     1.24.3           
pandas                    1.5.3 
node.js                   16.13.1
React                     8.1.2

The project mainly use 'REACT' as front-end frame and 'FLASK' as back-end frame.

!Second, how to build and runthis project?
    1.Download all the packages and frames We listed on top.
    2.Go to Terminal and run 'npm build'(only need to do at the first time)
    3.Continue run 'npm start', then you already start the front-end in localhost:3000
    4.Open another Terminal and run 'flask run', then you start back-end in localhost:5000
    5.Enjoy our shit website!(hope so)

!Third,how does this website work? What technology do we used？
    1. Flow:  Upload Drug's Img --------> Text Recognize the Img -------> Retrive most simailar Drug throw the Text------->Show the Information of the Drug
    2. Text Recognize:
        We mainly used the 'Tesseract OCR' package which is developed by Google to finish our OCR function.
    3. Text Retrival:
        Because the text we obtain from drug images often contains numerous errors and special characters, we need to preprocess these images. Initially, we define a function that takes a list of words (drug names) and a target word as parameters and returns the word most similar to the target word. The function utilizes the SequenceMatcher class from the difflib library in Python to compute similarity scores between words and replaces highly similar words with the target word. Next, another function iterates through a keyword list and searches for the word most relevant to each keyword, storing the scores in a dictionary. Finally, the function sorts the keywords by score from high to low and returns the highest-scoring keyword, which is our target drug name.