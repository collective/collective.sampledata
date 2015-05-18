from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage
 
 
class SampleData(BrowserPage):
    """
    """
 
    template = ViewPageTemplateFile('sampledata.pt')
 
    def __call__(self):
        return self.template()
