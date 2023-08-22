from treebeard.mp_tree import MP_NodeQuerySet


class CategoryQuerySet(MP_NodeQuerySet):
    def public(self):
        return self.filter(is_public=True)