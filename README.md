# EVM Wallet Generator

The EVM Wallet Generator is a Python script designed to automatically generate Ethereum Virtual Machine (EVM) wallets. Wallets can be created using either private keys or seed phrases, and the results can be saved to a CSV file.

---

## Features

- **Generate Wallets**:
  - Using **Private Keys**
  - Using **Seed Phrases**
- **Save Wallets** to a CSV file.
- **Display Wallets** interactively in the terminal using Rich Table.

---

## Prerequisites

1. Python 3.x installed on your computer.
2. Required libraries:
   - `eth-account`
   - `rich`

Install the required libraries using the following command:
```bash
pip install eth-account rich
```

---

## How to Use

1. Run the Python script:
   ```bash
   python <script_filename>.py
   ```
2. Follow the terminal instructions to choose the wallet generation method:
   - Type **1** to generate wallets with private keys.
   - Type **2** to generate wallets with seed phrases.
3. Enter the number of wallets you want to generate.
4. Choose whether to save the results to a CSV file.
5. If yes, specify the desired filename (e.g., `wallets.csv`).

---

## CSV File Structure

The generated CSV file will contain the following columns:

### If generated with **Private Keys**:
- **No**
- **Address** (Wallet Address)
- **Private Key**

### If generated with **Seed Phrases**:
- **No**
- **Address** (Wallet Address)
- **Seed Phrase**

---

## Example Terminal Output

```plaintext
Welcome to the EVM Wallet Generator!
Choose the wallet generation method:
[1] With Private Key
[2] With Seed Phrase
Enter your choice (1/2): 1
Enter the number of wallets to generate: 3

+----+------------------------------------------+------------------------------------------+
| No | Address                                  | Private Key                              |
+----+------------------------------------------+------------------------------------------+
| 1  | 0x1234567890abcdef1234567890abcdef123456 | 0xabcdefabcdefabcdefabcdefabcdefabcdef |
| 2  | 0xabcdef1234567890abcdef1234567890abcdef | 0x123456123456123456123456123456123456 |
| 3  | 0xabcdefabcdefabcdefabcdefabcdefabcdef   | 0xabcdefabcdefabcdefabcdefabcdefabcdef |
+----+------------------------------------------+------------------------------------------+

Wallets successfully saved to wallets.csv!
```

---

## Security Notes
- **Do not share CSV files** containing private keys or seed phrases with anyone.
- Ensure that the CSV file is stored in a secure location.

---

## License
This project is open-source and licensed under the [MIT License](https://opensource.org/licenses/MIT).
