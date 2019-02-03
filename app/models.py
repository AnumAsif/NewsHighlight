class News:
    '''
    News class to define News Objects
    '''

    def __init__(self, source_name, source_url, author_name, imageUrl, description, article, timeOfCreation):
        self.source_name=source_name
        self.source_url=source_url
        self.author_name=author_name
        self.imageUrl=imageUrl
        self.description=description
        self.article=article
        self.timeOfCreation=timeOfCreation
