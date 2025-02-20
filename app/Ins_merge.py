import os
import pandas as pd

input_dir = "/app/in/"
output_dir = "/app/out/"
instrument_file = os.path.join(input_dir, "InstrumentDetails.csv")
position_file = os.path.join(input_dir, "PositionDetails.csv")
output_file = os.path.join(output_dir, "PositionReport.csv")

os.makedirs(output_dir, exist_ok=True)

if not os.path.exists(instrument_file) or not os.path.exists(position_file):
    print("❌ ERROR: One or both input files are missing!")
    exit(1)

df_instrument = pd.read_csv(instrument_file)
df_position = pd.read_csv(position_file)

print("📂 Instrument File Columns:", df_instrument.columns.tolist())
print("📂 Position File Columns:", df_position.columns.tolist())

df_merged = df_position.merge(df_instrument, left_on="InstrumentID", right_on="ISIN", how="outer")
df_merged["Unit Price"] = df_merged["Unit_Price"] * df_merged["Quantity"]

print("✅ Merged Data Preview:\n", df_merged.head())
df_merged.to_csv("/app/out/PositionReport.csv", index=False)