#sending a email to a friend
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("dixitshetty930@gmail.com", "**********")
msg = "HI"
server.sendmail("dixitshetty930@gmail.com","vikramgowda02@gmail.com",msg)
server.quit()
