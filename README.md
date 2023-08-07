###In this project, I built a website to retrival drugs information base on their pictures!###

##!First, let me list the package and frame's version:##

python                    3.9.16  
flask                     2.2.2            
numpy                     1.24.3           
pandas                    1.5.3 
node.js                   16.13.1
React                     8.1.2

The project mainly use #'REACT'# as front-end frame and #'FLASK'# as back-end frame.

##Second, how to build and runthis project?##
    1.Download all the packages and frames We listed on top.  
    2.Go to Terminal and run 'npm build'(only need to do at the first time)  
    3.Continue run 'npm start', then you already start the front-end in localhost:3000  
    4.Open another Terminal and run 'flask run', then you start back-end in localhost:5000  
    5.Enjoy the shit project!(hope so)  

##Third,how does this website work? What technology do we used？##
    1. Flow:  Upload Drug's Img --------> Text Recognize the Img -------> Retrive most simailar Drug throw the Text------->Show the Information of the Drug  
    2. Text Recognize:  
        We mainly used the 'Tesseract OCR' package which is developed by Google to finish our OCR function.  
    3. Text Retrival:  
        Preprocess the target word and sentence -------> Check with key words ------> Get scores and choose the best predict drug ------> Get the drug's information
