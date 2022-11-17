import pandas as pd
import uvicorn
from fastapi import FastAPI

from constants import GEO_CODES

app = FastAPI()


@app.get("/country/{iso_code}")
async def get_country(iso_code: str):
    if iso_code.upper() in GEO_CODES.keys():
        gdp_dataframe, srp_dataframe = pd.read_excel("GDP.xlsx"), pd.read_excel(
            "SRP.xlsx"
        )
        data_gdp = gdp_dataframe[gdp_dataframe["GEO (Codes)"] == iso_code.upper()][
            "2021"
        ]
        data_srp = srp_dataframe[srp_dataframe["GEO (Codes)"] == iso_code.upper()][
            "Interval"
        ]
        return {
            "Country": GEO_CODES[iso_code.upper()],
            "ISO_CODE": iso_code.upper(),
            f"GDP 2021 value for {iso_code.upper()}": int(data_gdp.values[0]),
            f"Youngest coding age range for {iso_code.upper()}": f"{data_srp.values[0]} years",
        }
    else:
        return {"Not existing EU country"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
