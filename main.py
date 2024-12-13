import serial

# Настройки UART
UART_PORT = "/dev/serial0"  # Убедитесь, что используется правильный порт
BAUD_RATE = 115200          # Скорость передачи данных джойстика

def process_data(raw_data):
    """
    Обработка данных, поступивших через UART.
    """
    try:
        # Пытаемся декодировать данные как текст
        decoded_data = raw_data.decode('utf-8')
        print(f"Получено (текст): {decoded_data}")
    except UnicodeDecodeError:
        # Если декодирование не удалось, выводим как байты
        print("Получено (байты):", " ".join(f"{byte:02x}" for byte in raw_data))
        analyze_bytes(raw_data)

def analyze_bytes(byte_data):
    """
    Анализ данных в формате байтов.
    """
    # Пример анализа данных
    if len(byte_data) >= 3:
        # Определение команды и значений
        command = byte_data[0]
        values = byte_data[1:]
        print(f"Команда: {command:02x}, Значения: {[f'{v:02x}' for v in values]}")
    else:
        print("Недостаточно данных для анализа.")

try:
    # Инициализация последовательного порта
    with serial.Serial(UART_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Открыт порт {UART_PORT} с скоростью {BAUD_RATE}")

        while True:
            if ser.in_waiting > 0:  # Проверяем, есть ли входящие данные
                raw_data = ser.read(ser.in_waiting)  # Читаем все доступные данные
                process_data(raw_data)
            else:
                pass  # Небольшая задержка не обязательна
except serial.SerialException as e:
    print(f"Ошибка последовательного порта: {e}")
except KeyboardInterrupt:
    print("Программа завершена пользователем.")
