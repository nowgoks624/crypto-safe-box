"""
OPReturnHunter: поиск и анализ OP_RETURN данных в транзакциях Bitcoin-адреса.
"""

import requests
import argparse
import binascii

def get_transactions(address):
    url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}?transaction_details=true"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Не удалось получить список транзакций.")
    return r.json()["data"][address]["transactions"]

def get_tx_outputs(txid):
    url = f"https://api.blockchair.com/bitcoin/raw/transaction/{txid}"
    r = requests.get(url)
    if r.status_code != 200:
        return []
    return r.json()["data"][txid]["decoded_raw_transaction"].get("vout", [])

def extract_opreturn_data(outputs):
    opreturn_data = []
    for out in outputs:
        script = out.get("script_pub_key", {}).get("asm", "")
        if "OP_RETURN" in script:
            parts = script.split()
            try:
                index = parts.index("OP_RETURN")
                if len(parts) > index + 1:
                    raw_hex = parts[index + 1]
                    decoded = binascii.unhexlify(raw_hex).decode(errors="ignore")
                    opreturn_data.append((raw_hex, decoded))
            except:
                continue
    return opreturn_data

def analyze_opreturns(address):
    print(f"🔎 Поиск OP_RETURN в транзакциях адреса: {address}")
    txs = get_transactions(address)
    found = 0
    for txid in txs[:30]:
        outputs = get_tx_outputs(txid)
        op_data = extract_opreturn_data(outputs)
        for hexdata, text in op_data:
            found += 1
            print(f"
📦 TXID: {txid}")
            print(f"HEX: {hexdata}")
            print(f"TXT: {text}")
    if not found:
        print("❌ OP_RETURN данные не найдены.")
    else:
        print(f"
✅ Найдено {found} OP_RETURN выходов.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OPReturnHunter — анализ OP_RETURN данных.")
    parser.add_argument("address", help="Bitcoin-адрес")
    args = parser.parse_args()
    analyze_opreturns(args.address)
