import pandas as pd
from pp_exec_env.base_command import BaseCommand, Syntax
from otlang.sdk.syntax import Positional, Keyword, OTLType


class OrderByCommand(BaseCommand):
    syntax = Syntax(
        [
            Positional(name="columns", otl_type=OTLType.TEXT, inf=True),
            Keyword(name="asc", key="ascending", otl_type=OTLType.ALL, required=False)
        ]
    )

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        asc = self.get_arg('asc').value
        if asc is None:
            asc = True
        else:
            asc = bool(asc)
        df.sort_values(by=[c.value for c in self.get_iter('columns')], axis=0, ascending=asc, inplace=True)
        return df
