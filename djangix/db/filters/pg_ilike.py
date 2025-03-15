from django.db.models.lookups import IContains


class PostgresILike(IContains):
    """ Аналогично like, но не чувствителен к регистру """

    lookup_name = "ilike"

    def as_postgresql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        return f"{lhs} ILIKE {rhs}", lhs_params + rhs_params
