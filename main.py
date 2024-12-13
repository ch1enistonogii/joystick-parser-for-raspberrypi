import serial

# Настройки UART
UART_PORT = "/dev/serial0"  # Убедитесь, что используется правильный порт
BAUD_RATE = 115200          # Скорость передачи данных джойстика

try:
    # Инициализация последовательного порта
    with serial.Serial(UART_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Открыт порт {UART_PORT} с скоростью {BAUD_RATE}")

        while True:
            if ser.in_waiting > 0:  # Проверяем, есть ли входящие данные
                raw_data = ser.read(ser.in_waiting)  # Читаем все доступные данные
                try:
                    # Пытаемся декодировать данные как текст
                    decoded_data = raw_data.decode('utf-8')
                    print(f"Получено (текст): {decoded_data}")
                except UnicodeDecodeError:
                    # Если декодирование не удалось, выводим как байты
                    print("Получено (байты):", " ".join(f"{byte:02x}" for byte in raw_data))
            else:
                pass  # Небольшая задержка не обязательна
except serial.SerialException as e:
    print(f"Ошибка последовательного порта: {e}")
except KeyboardInterrupt:
    print("Программа завершена пользователем.")
