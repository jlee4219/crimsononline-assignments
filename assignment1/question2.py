class Article:
    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file

    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''
    def __init__(self, headline, content, creator, related_image = None):
        self.headline = headline
        self.content = content
        self.creator = creator
        self.related_image = related_image

    def show(self):
        print self.content
        if self.related_image != None:
            self.related_image.show()

    # I'm using the headline to save the file. Hopefully two articles don't have the same headline?
    # The other thought I had is indexing the files, but this would take more memory.
    def save(self):
        import json
        repr = self.__dict__
        if self.related_image != None:
            repr['related_image'] = self.related_image.__dict__
        open(self.headline + ".txt", 'w').write(json.dumps(repr))

    @classmethod
    def load(cls, filename):
        try:
            import json
            article = json.load(open(filename,'r'))
            if article['related_image'] != 'null':
                im = Picture(article['related_image']['image_file'],
                             article['related_image']['creator'])
            else:
                im = None
            return cls(article["headline"], article["content"], article["creator"], im)
        except IOError:
            print "Could not load article."
    pass

class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
    def __init__(self, image_file, creator):
        self.image_file = image_file
        self.creator = creator

    def show(self):
        from PIL import Image
        im = Image.open(self.image_file)
        im.show()
    pass
