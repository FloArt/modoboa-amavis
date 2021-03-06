class AmavisRouter(object):

    """A router to control all database operations on models in
    the amavis application"""

    def db_for_read(self, model, **hints):
        """Point all operations on amavis models to 'amavis'."""
        if model._meta.app_label == 'modoboa_amavis':
            return 'amavis'
        return None

    def db_for_write(self, model, **hints):
        """Point all operations on amavis models to 'amavis'."""
        if model._meta.app_label == 'modoboa_amavis':
            return 'amavis'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation if a model in amavis is involved."""
        if obj1._meta.app_label == 'modoboa_amavis' \
           or obj2._meta.app_label == 'modoboa_amavis':
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'amavis'
        database.
        """
        if db == "amavis":
            return app_label == "modoboa_amavis"
        return None
