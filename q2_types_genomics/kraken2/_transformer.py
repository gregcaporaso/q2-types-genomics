# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pandas as pd

from . import Kraken2ReportFormat
from ..plugin_setup import plugin


@plugin.register_transformer
def _1(ff: Kraken2ReportFormat) -> pd.DataFrame:
    df, cols = ff._to_dataframe()
    df.columns = cols.keys()
    return df
