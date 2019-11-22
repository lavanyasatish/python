import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls() 
pw=input("enter pw") 

s.login("lavanya.satish29@gmail.com", pw) 
  
 
message = "python email sending program"
  

s.sendmail("lavanya.satish29@gmail.com", "lavanya.16cs@cmr.edu.in", message) 
  
 
s.quit() 
