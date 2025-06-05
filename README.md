# OPReturnHunter

**OPReturnHunter** — инструмент для извлечения и анализа `OP_RETURN` данных из транзакций по Bitcoin-адресу.

## Что такое OP_RETURN?

`OP_RETURN` — это способ записывать произвольные данные в блокчейн. Он используется:
- для записи метаданных,
- NFT/токенов (Omni, Counterparty),
- скрытых сообщений или хэшей.

## Возможности

- Получение всех транзакций адреса
- Извлечение OP_RETURN выходов
- Декодирование данных в текст

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python opreturnhunter.py <bitcoin_address>
```

Пример:

```bash
python opreturnhunter.py 1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY
```

## Примечание

Обрабатываются только последние 30 транзакций.

## Лицензия

MIT License
