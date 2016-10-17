from Controller.indexPageController import IndexPage
from Controller.menuBarController import MenuBar
from Controller.singleDetailPageController import SingleDetailPage

__author__ = 'kzhu'

class Runner(IndexPage,MenuBar,SingleDetailPage):
    def __init__(self):
        super(Runner,self).__init__()
