from ...widgets.layout_wrap import LayoutWrap
    

class ModalLayoutWrap(LayoutWrap):
    
    def signal(self, **kwargs):
        pass
    
    def hide(self, *, every: bool = False):
        self.window.hideModal(every=every)
    