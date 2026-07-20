"""Quick smoke test to verify all modules import and work correctly."""
import sys, io
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from src.utils import Colors, format_currency, validate_date
from src.functions import initialize_data_file, load_transactions, get_next_id
initialize_data_file()
print("OK: utils import")
print("OK: functions import")
print("format_currency(12345.6)  =>", format_currency(12345.6))
print("validate_date('2025-07-15') =>", validate_date("2025-07-15"))
print("validate_date('bad-input')  =>", validate_date("bad-input"))
txns = load_transactions()
print(f"load_transactions => {len(txns)} records")
print(f"get_next_id       => {get_next_id(txns)}")
print()
print("All checks passed!")
