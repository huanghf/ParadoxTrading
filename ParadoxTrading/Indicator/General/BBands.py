import statistics
from collections import deque

from ParadoxTrading.Indicator.IndicatorAbstract import IndicatorAbstract
from ParadoxTrading.Utils import DataStruct


class BBands(IndicatorAbstract):
    def __init__(
            self, _period: int = 26, _use_key: str = 'closeprice',
            _rate: float = 2.0, _idx_key: str = 'time',
            _ret_key=('upband', 'midband', 'downband')
    ):
        super().__init__()

        self.use_key = _use_key
        self.idx_key = _idx_key
        self.keys = [self.idx_key] + list(_ret_key)

        self.data = DataStruct(
            self.keys, self.idx_key
        )

        self.period = _period
        self.rate = _rate
        self.buf = deque(maxlen=self.period)

    def _addOne(self, _data_struct: DataStruct):
        index_value = _data_struct.index()[0]
        self.buf.append(_data_struct.getColumn(self.use_key)[0])
        mean = statistics.mean(self.buf)
        std = statistics.pstdev(self.buf, mu=mean)
        self.data.addRow([
            index_value, mean + self.rate * std, mean, mean - self.rate * std
        ], self.keys)
