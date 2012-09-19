from zope.interface import implements
from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.interfaces import NotFound

class TransporterTraverser(object):
    
    implements(IPublishTraverse)
    
    def __init__(self, context, request):

        import pdb; pdb.set_trace()

        self.context = context
        self.objects = context['go']
        self.object_ids = self.objects.objectIds()
        self.request = request
    
    def publishTraverse(self, request, name):
        
        import pdb; pdb.set_trace()
        
        if name in self.object_ids:
            return self.objects.get(name).__of__(self.context)
        else:
            raise NotFound
