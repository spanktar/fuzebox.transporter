from zope.interface import implements
from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.interfaces import NotFound
from ZPublisher.BaseRequest import DefaultPublishTraverse

class TransporterTraverser(object):
    
    implements(IPublishTraverse)
    
    def __init__(self, context, request):

        self.context = context
        self.objects = context['go']
        self.object_ids = self.objects.objectIds()
        self.request = request
    
    def publishTraverse(self, request, name):
                
        if name in self.object_ids:
            return self.objects.get(name).__of__(self.context)
        else:
            
            import pdb; pdb.set_trace()
            
            default_adapter = DefaultPublishTraverse(object, self)
            ob2 = default_adapter.publishTraverse(self, name)
            return ob2
            
        