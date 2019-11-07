class AnimatedSprite:
    def __init__(self,img_file,x,y,width,height,frames,frameLength):
        self.rects = [(i * width + x,y,width + x,height + y) for i in range(frames)]
        self.images = pyganim.getImagesFromSpriteSheet(img_file,rects=self.rects)
        # alter spritesheet
        self.images = [pygame.transform.scale2x(image) for image in self.images]
        self.frames = list(zip(self.images, [frameLength] * len(self.images)))
        self.animObj = pyganim.PygAnimation(self.frames)

    def getAnimatedSprite(self):
        return self.animObj
