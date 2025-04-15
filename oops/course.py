class course:
    def __init__(self,course_name,course_duration,*books):
        self.course_name= course_name
        self.duration= course_duration
        self.books = [self.books(b) for b in  books]
    def show_details(self):
        print('name:', self.course_name)
        print('duration:',self.duration)
        print('suggested books')
        for b in self.books:
            print(b)

    class books:
        def __init__(self,title,):
            self.title = title

        def __str__(self):
            return self.title
c1=course('python', 10, 'pyth''java''c')
c1.show_details()