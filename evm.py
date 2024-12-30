import csv
from eth_account import Account
from rich.console import Console
from rich.table import Table

# Initialize Rich console
console = Console()

# Enable Mnemonic Feature
Account.enable_unaudited_hdwallet_features()

def generate_wallets_with_private_key(count):
    wallets = []
    for _ in range(count):
        account = Account.create()
        wallets.append({
            'address': account.address,
            'private_key': account.key.hex()
        })
    return wallets

def generate_wallets_with_seed_phrase(count):
    wallets = []
    for _ in range(count):
        account, mnemonic = Account.create_with_mnemonic()
        wallets.append({
            'address': account.address,
            'seed_phrase': mnemonic
        })
    return wallets

def save_to_csv(wallets, filename):
    keys = wallets[0].keys()
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(wallets)

    console.print(f"[green]Wallets successfully saved to file [bold]{filename}[/bold]![green]")

def display_wallets(wallets):
    table = Table(title="Generated Wallets")

    # Add columns based on wallet type
    table.add_column("No", style="cyan")
    table.add_column("Address", style="magenta")
    if 'private_key' in wallets[0]:
        table.add_column("Private Key", style="yellow")
    elif 'seed_phrase' in wallets[0]:
        table.add_column("Seed Phrase", style="yellow")

    # Add rows of data
    for i, wallet in enumerate(wallets, 1):
        if 'private_key' in wallet:
            table.add_row(str(i), wallet['address'], wallet['private_key'])
        elif 'seed_phrase' in wallet:
            table.add_row(str(i), wallet['address'], wallet['seed_phrase'])

    console.print(table)

def main():
    console.print("[bold cyan]Welcome to the EVM Wallet Generator![bold cyan]")
    console.print("Choose a wallet generation method:")
    console.print("[1] Using Private Key")
    console.print("[2] Using Seed Phrase")

    while True:
        try:
            choice = int(input("Enter your choice (1/2): "))
            if choice not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            console.print("[red]Invalid choice. Enter 1 or 2![red]")

    while True:
        try:
            count = int(input("Enter the number of wallets to generate: "))
            if count <= 0:
                raise ValueError
            break
        except ValueError:
            console.print("[red]Enter a valid positive number![red]")

    wallets = []
    if choice == 1:
        wallets = generate_wallets_with_private_key(count)
    elif choice == 2:
        wallets = generate_wallets_with_seed_phrase(count)

    display_wallets(wallets)

    save_option = input("Do you want to save the results to a CSV file? (y/n): ").lower()
    if save_option == 'y':
        filename = input("Enter the file name (e.g., wallets.csv): ")
        if not filename.endswith('.csv'):
            filename += '.csv'
        save_to_csv(wallets, filename)

if __name__ == "__main__":
    main()
