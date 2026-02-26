class Book :
    def __init__(self,title,author,list_of_review):
        self.title = title
        self.author = author
        self.list_of_review = list_of_review

    def new_review(self,review):
        self.list_of_review.append(review)
        print("Review added sucesfully.")

    def count_review(self):
        print("review count :",len(self.list_of_review))


    def display_all_review(self):
        print("All Review : ")
        for review in self.list_of_review:
            print("-",review)

book1 = Book("Teal of Naruto Uzumaki!","Juraya",[])
book1.new_review("GOOD BOOK")
book1.display_all_review()
book1.new_review("Super Amezing")
book1.display_all_review()
