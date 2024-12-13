import serial

# Настройка последовательного порта
port = "/dev/serial0"
baudrate = 115200
ser = serial.Serial(port, baudrate, timeout=1)

print(f"Открыт порт {port} с скоростью {baudrate}")

buffer = b""  # Буфер для данных

while True:
    try:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting)
            buffer += data  # Добавляем данные в буфер

            # Декодируем текст для отображения (если это текст)
            try:
                text_data = data.decode('utf-8')
                print(f"Получено (текст): {text_data}")
            except UnicodeDecodeError:
                print(f"Получено (байты): {data.hex()}")

            # Пытаемся обработать данные в буфере
            while len(buffer) >= 3:  # Минимальная длина данных для анализа
                command = buffer[0]  # Первый байт - команда
                values = buffer[1:3]  # Следующие два байта - значения

                print(f"Команда: {command:02x}, Значения: {[f'{v:02x}' for v in values]}")
                buffer = buffer[3:]  # Убираем обработанные данные из буфера

    except KeyboardInterrupt:
        print("Выход из программы.")
        break
    except Exception as e:
        print(f"Ошибка: {e}")
