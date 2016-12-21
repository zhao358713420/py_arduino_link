import serial

#连接arduino
ser = serial.Serial('COM3', 9600)

#从arduino中读取信息
def get_info_from_arduino():
    line = ""
    while len(line) == 0:
        line = ser.readline()
    data = [int(val) for val in line.split()]
    return data

def main():
    while True:
        data = get_info_from_arduino()
        print(data)

if __name__ == '__main__':
    main()