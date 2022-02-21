from pp_exec_env.base_command import BaseCommand, Syntax, Rule, pd


class OrderByCommand(BaseCommand):
    syntax = Syntax(
        [
            Rule(name="columns", type="arg", input_types=['string', 'term'], inf=True),  # must_be_a_field=True
            Rule(name="asc", type="kwarg", key="ascending", input_types=['integer'], required=False)

        ],
        use_timewindow=False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        asc = self.get_arg('asc').value != 0

        for column in self.get_arg('columns'):
            df.sort_values(column.value, axis=1, ascending=asc, inplace=True)

        return df
