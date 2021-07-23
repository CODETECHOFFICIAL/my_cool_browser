import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('mihir.patilmihir14@gmail.com', 'Mihir@119')
server.sendmail('mihir.patilmihir14@gmail.com',
                'mihir.patilmihir598@gmail.com',
                'Hi , thanks for appreciating')