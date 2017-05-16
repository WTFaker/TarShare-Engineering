import serial
 
def send_text(number, text, path='/dev/ttyUSB0'):
    ser = serial.Serial(path, timeout=1)
    # set text mode
    ser.write('AT+CMGF=%d\r' % 1)
    # set number
    ser.write('AT+CMGS="%s"\r' % number)
    # send message
    ser.write('%s\x1a' % text)
    print ser.readlines()
    ser.close()
 
send_text('09087588***', 'hey how are you?')
