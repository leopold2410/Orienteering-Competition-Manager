from orator.migrations import Migration


class CreateCompetitionTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Competition') as table:
            table.increments('id')
            table.string('name')
            table.text('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Competition')
