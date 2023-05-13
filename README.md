# FYP (Handwriting Based Writer Identification using SVM Model)
I have done this Project with dedication and hard work in My FYP (Final Year Project) by taking help from Internet (ChatGPT).


To run this code in Your machine you have to open Google Colab and there is no libraries issues (importing issues and also there is no need to install any library for this project)

Steps to Run this Project
1. Collect the Dataset of handwriting and save it in Google drive in directory Writers which is subdirectory of Data (Data is the main Directory). If you change the name of directory then make sure to change the path in code as well.
2. Open Handwriting_Based_Writer_Identification.ipynb file in Google Colab
3. Run the Code Step by Step in Google Colab
4. It takes time while preprocessing and Augmentation Techniques as these steps also save the images in Drive
5. Make Sure you must have atleast enough space according to the dataset (i have upload only dataset of few persons for only using to test the working you can use yours)
6. After Training you are able to save the trained model which then also is useable in frontend to identify the name of writer on new test image.
7. When you save the trained model (svm_model.pkl) after training is done in Google drive the next cell in Colab is to predict the name on the new test image. (Make sure you change the path of test image according to where you save the image for test in your Google Drive).
8. This trained model is used in frontend as well by downloading it and place that model in Frontend directory.
