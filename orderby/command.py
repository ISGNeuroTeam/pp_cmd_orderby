import pandas as pd
from pp_exec_env.base_command import BaseCommand, Syntax
from otlang.sdk.syntax import Positional, Keyword, OTLType


class OrderByCommand(BaseCommand):
    syntax = Syntax(
        [
            Positional(name="columns", otl_type=OTLType.TEXT, inf=True),
            Keyword(name="asc", key="ascending", otl_type=OTLType.INTEGER, required=False)
        ],
        use_timewindow=False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        asc = self.get_arg('asc').value != 0

        for column in self.get_iter('columns'):
            df.sort_values(column.value, axis=1, ascending=asc, inplace=True)

        return df
