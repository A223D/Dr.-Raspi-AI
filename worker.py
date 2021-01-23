print(tf.__version__)

result = "invalid"
body = "There is nothing here"
lcd.clear()
lcd.message("Click button\nfor picture")
button.wait_for_press()

print("Here")
camera.start_preview()
sleep(2)
camera.capture("./picture.jpg")
camera.stop_preview()

print("Done")

def predictDisease(imPath):
    img = Image.open(imPath).resize((125, 100))
    imgArr = np.asarray(img)
    #x = np.expand_dims(x, axis =0)
    ready = np.expand_dims(imgArr, axis=0)
    readyMean = np.mean(ready)
    readyStd = np.std(ready)
    ready = (ready-readyMean)/readyStd
   # print(ready.shape)
    #print(ready)
    classes = model.predict(ready).tolist()
    maxVal = max(classes[0])
   # print(maxVal)
   # print(classes[0])
    ans=classes[0].index(maxVal)
    print(maxVal*100)
    result = lesion_type_dict[ans]
    
    print(result)
    f=open("answer.txt", "w")
    f.write(result+" "+str((maxVal*100))+"%")
    f.close()
    body = result+" "+str((maxVal*100))
    print(body)
    lcd.clear()
    lcd.set_cursor(0,0)
    lcd.message(result)
    lcd.set_cursor(0,1)
    lcd.message(str(maxVal*100))
    sleep(5)
    lcd.clear()
    lcd.set_cursor(0,0)
    lcd.message("Working...")
    
    
    #images = np.vstack([x])
    #print("Running model now")
    #classes = model.predict(images, batch_size =10)
    #print(classes[0])
    
predictDisease("./picture.jpg")
exec(open("./sender.py").read())
