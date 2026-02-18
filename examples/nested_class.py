from selv import selv


@selv
class Child:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Child(value={self.value})"


@selv
class Parent:
    def __init__(self):
        self.child = Child(100)


parent = Parent()
parent.child.value = 200

print("\nParent class changelog:")
parent_changelog = parent.view_changelog()
print(parent_changelog)

print("\nChild class changelog:")
child_changelog = parent.child.view_changelog()
print(child_changelog)
