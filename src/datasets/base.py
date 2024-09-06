from typing import Callable




class ListDataset[S, O ]:

    def __init__(self, data: list[S], transform: Callable[[S], O]) -> None:
        self._data =  data
        self._transform = transform

    def __len__(self) -> int: return len(self._data)

    def __getitem(self, index: int) -> O:
        return self._transform(self._data[index]) 

