import requests

def parse_data(wallet_address):
    url = f"https://kx58j6x5me.execute-api.us-east-1.amazonaws.com/scroll/bridge-balances?walletAddress={wallet_address}"
    try:
        response = requests.get(url)
        data = response.json()
        points_sum = sum(item.get("points", 0) for item in data)  # Суммируем значения points из каждого объекта
        return points_sum
    except Exception as e:
        return f"Error: {e}"

def main():
    # Чтение списка кошельков из файла
    with open("wallets.txt", "r") as file:
        wallets = file.read().splitlines()

    # Парсинг значений для каждого кошелька
    for wallet_address in wallets:
        parsed_data = parse_data(wallet_address)
        if isinstance(parsed_data, (int, float)):  # Проверяем, что возвращено число
            print(f"Total points for {wallet_address}: {parsed_data}")
        else:
            print(parsed_data)

if __name__ == "__main__":
    main()
