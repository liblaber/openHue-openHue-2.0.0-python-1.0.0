# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .error import Error
from .scene_get import SceneGet


@JsonMap({})
class GetScenesOkResponse(BaseModel):
    """GetScenesOkResponse

    :param errors: errors, defaults to None
    :type errors: List[Error], optional
    :param data: data, defaults to None
    :type data: List[SceneGet], optional
    """

    def __init__(self, errors: List[Error] = None, data: List[SceneGet] = None):
        if errors is not None:
            self.errors = self._define_list(errors, Error)
        if data is not None:
            self.data = self._define_list(data, SceneGet)
