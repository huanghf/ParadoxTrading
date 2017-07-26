import numpy as np

from ParadoxTrading.Utils import DataStruct


def sharpRatio(
        _fund: DataStruct,
        _factor: int = 252,
        _unrisk_return_ratio: float = 0.0,
        _fund_index: str = 'total_fund'
) -> float:
    fund = _fund[_fund_index]
    return_ratio = np.array(fund[1:]) / np.array(
        fund[:-1]) - 1.0 - _unrisk_return_ratio
    return (
        np.mean(return_ratio) / np.std(return_ratio)
        * np.sqrt(_factor)
    ).tolist()
