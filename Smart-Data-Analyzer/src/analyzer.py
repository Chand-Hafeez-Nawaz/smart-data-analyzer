
import io
from typing import Union, Dict, Any, List
import pandas as pd

class SmartDataAnalyzer:
    """
    Core analysis class.
    Accepts a file path or a file-like object (BytesIO/StringIO) for CSV/Excel.
    """
    def __init__(self, file: Union[str, io.BytesIO, io.StringIO]):
        self.data = self._load(file)

    def _load(self, file: Union[str, io.BytesIO, io.StringIO]) -> pd.DataFrame:
        # If it's a path string, branch by extension
        if isinstance(file, str):
            if file.lower().endswith(".csv"):
                return pd.read_csv(file)
            elif file.lower().endswith((".xlsx", ".xls")):
                return pd.read_excel(file)
            else:
                raise ValueError("Unsupported file extension. Use .csv or .xlsx")
        # Otherwise, try CSV then Excel
        if hasattr(file, "seek"):
            # Try CSV first
            try:
                file.seek(0)
                return pd.read_csv(file)
            except Exception:
                pass
            # Try Excel
            file.seek(0)
            return pd.read_excel(file)
        raise ValueError("Unsupported file type provided")

    def basic_info(self) -> Dict[str, Any]:
        return {
            "rows": int(self.data.shape[0]),
            "columns": int(self.data.shape[1]),
            "column_names": [str(c) for c in self.data.columns],
            "dtypes": {str(k): str(v) for k, v in self.data.dtypes.to_dict().items()},
            "missing_values": {str(k): int(v) for k, v in self.data.isna().sum().to_dict().items()},
        }

    def statistics(self) -> Dict[str, Dict[str, Any]]:
        # describe with numeric_only where applicable (pandas >=1.5 uses numeric_only param)
        desc = self.data.describe(include='all', datetime_is_numeric=True)
        # Convert DataFrame to nested dict and ensure JSON-serializable types
        out = {col: {str(idx): (val.item() if hasattr(val, "item") else (None if pd.isna(val) else val))
                     for idx, val in series.items()}
               for col, series in desc.to_dict().items()}
        return out

    def correlation(self) -> Dict[str, Dict[str, float]]:
        corr = self.data.corr(numeric_only=True)
        return corr.to_dict()

    def numeric_columns(self) -> List[str]:
        return [c for c in self.data.columns if pd.api.types.is_numeric_dtype(self.data[c])]
