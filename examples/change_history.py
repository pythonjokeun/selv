from selfie import selfie


@selfie
class Document:
    def __init__(self, title):
        self.title = title
        self.content = ""
        self.version = 1


doc = Document("Untitled")
doc.content = "Hello world"
doc.version = 2
doc.title = "My Document"

print("All changes (flat format):")
for change in doc.get_change_history():
    print(f"  {change['attr']}: {change['from']} -> {change['to']}")

print("\nGrouped by attribute:")
grouped = doc.get_change_history(format="attr")
for attr, changes in grouped.items():
    print(f"  {attr}: {len(changes)} changes")

print("\nTitle changes only:")
for change in doc.get_change_history("title"):
    print(f"  {change['from']} -> {change['to']}")
