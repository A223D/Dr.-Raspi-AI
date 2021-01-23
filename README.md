## Please do NOT use Dr. Raspi AI in place of a trained medical professional. This is a hackathon project and not a professional diagnosis tool.

## Inspiration
Due to recent times, hospital staff is engaged with COVID concerns and is not able to provide the assistance it used to during pre-COVID times. Acute care wards of many major hospitals are running above 95% occupancy. Doctors and major nurses are busy attending to COVID patients while out-patients with other concerns are placed later in the priority order.
Additionally hospital transmission of COVID-19 goes both ways. Even a doctor is at equal risk.
These problems, while not as big as COVID itself, deserve to be addressed, as they are adding to the problems faced by the general public.

## What it does
Dr. Raspi AI is a low-cost all-in-one package that looks at a diseased area of skin, and reports the probability of a patient having a skin disease. Depending on the probability of disease, the patient will be sent to see a doctor for a professional diagnosis. If the probability is low, the patient may not need to see a doctor. In a nutshell, our solution **decreases the risk of hospital transmission of diseases**, as there is no contact, as well as **saves the doctor’s time** for negative diagnoses. 

The report and picture is also sent to the patient's email ID as a record as well as future reference. The patient can keep this picture or it can be forwarded to the doctor if the probability is high. 

## How we built it
The first step was to train a machine learning model on a dataset of diseases. We decided to go with skin diseases, as they require skin contact, which is dangerous in these times. The dataset we chose is the [HAM10000 dataset](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000), which classifies seven types of skin diseases:
* Melanocytic nevi
* Melanoma
* Benign keratosis-like lesions
* Basal cell carcinoma
* Actinic keratoses
* Vascular lesions
* Dermatofibroma

We trained a convolutional neural network based model on the dataset using Google Colaboratory, since the Raspberry Pi is not powerful for that purpose. The model was then transferred to the Raspberry Pi for prediction and classification of images. Here are some statistics related to the training of our model. 
![alt text](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/362/255/datas/gallery.jpg)

We also designed a case for the entire solution in SolidWorks. Here is what the project was supposed to look like. 
![alt text](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/362/270/datas/gallery.jpg)

However, we made some mistakes and our 3D printed model did not fit our solution :(
![alt text](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/362/273/datas/gallery.jpg)

After that, we experimented with gpiozero and Adafruit LCD library for the Raspberry Pi to interface with the LCD screen and the button. After some fiddling and trial and error, we were able to display to statuses on the LCD screen and click pictures on the press of the button and classify it using our model.

The last step was email integration. For this, we set up a Gmail account for the Dr. Raspi AI: dr.raspi@gmail.com. Sending emails to this account will activate this device and ready it to click the picture for prediction. Theoretically, the nurse is going to send emails to the Dr. Raspi AI account. The format of the activation email is as follows:
* To: dr.raspi@gmail.com
* Subject: (patient's email address)

The patient's email is needed for record purposes. It is also where final report and picture is sent after the prediction is shown on the LCD screen.

## Challenges we ran into
* We are team of 4, where almost everyone is situated in different countries. Two of our team members are in India. One is in Canada, and the other is in Saudi Arabia. Communication was difficult, as we were based across 3 different timezones.
* The 3D printed case did not fit the dimensions that we needed. Hence, we had to continue without it. 
* Figuring how to sense new emails on the account, as well as attaching the picture and sending it to the patient's email address was a complex challenge, and a lot of time and effort was spent on this part. 

## Accomplishments that we're proud of
* Our model is 75% accurate!
* Actually completing the project, since there were a lot of moving parts from very different disciplines. Making everything work together synchronously and without delays tested our patience. 

## What we learned
* Sending and receiving emails on a Gmail account using Python on a Raspberry Pi (SMTP/IMAP)
* Interfacing LCD screens with Raspberry Pi.
* 3D printing is not as simple as it seems.

## What's next for Dr. Raspi AI
* Fixing the 3D printed case design and fitting all the electronics inside. 
* Adding more diseases to the model, improving the general usability of the solution.
