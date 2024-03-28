from project import Category
from project import Topic


class Document:

    def __init__(self, _id: int, category_id: int, topic_id: int, file_name: str):
        self.id = _id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, _id: int, category: Category, topic: Topic, file_name: str):
        return cls(_id, category.id, topic.id, file_name)

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)

    def edit(self, new_file_name: str):
        self.file_name = new_file_name

    def __repr__(self):
        return (f"Document {self.id}: {self.file_name}; "
                f"category {self.category_id}, "
                f"topic {self.topic_id}, "
                f"tags: {', '.join(self.tags)}"
)