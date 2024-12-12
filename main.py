import serial

# Настройки UART
UART_PORT = "/dev/serial0"  # Убедитесь, что используется правильный порт
BAUD_RATE = 115200          # Замените на скорость передачи данных вашего джойстика

try:
    # Инициализация последовательного порта
    with serial.Serial(UART_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Открыт порт {UART_PORT} с скоростью {BAUD_RATE}")

        while True:
            if ser.in_waiting > 0:  # Проверяем, есть ли входящие данные
                data = ser.read(ser.in_waiting)  # Читаем все доступные данные
                print(f"Получено: {data}")
            else:
                # Если данных нет, можно поставить небольшую задержку
                pass
except serial.SerialException as e:
    print(f"Ошибка последовательного порта: {e}")
except KeyboardInterrupt:
    print("Программа завершена пользователем.")
