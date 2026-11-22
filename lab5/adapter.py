
class OldArtifact:
    def cast_spell(self):
        print("Артефакт выпустил огненный шар")


class ArtifactAdapter:
    def __init__(self, artifact):
        self.artifact = artifact

    def use(self):
        self.artifact.cast_spell()


class MagicBook:
    def use(self):
        print("Герой использовал магическую книгу")


def use_item(item):
    item.use()

book = MagicBook()
old_artifact = OldArtifact()
artifact = ArtifactAdapter(old_artifact)

use_item(book)
use_item(artifact)
