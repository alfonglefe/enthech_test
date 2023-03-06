class SearchItem:
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

    def __str__(self):
        return f"\"{self.title}\", {self.description}, \n \t {self.url}"
