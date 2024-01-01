class SVG():
    def __init__(self):
        self._render_queue = [] # array of components to be rendered, in order
        self.res = '<svg id="final" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" width="400" height="200" style="border-radius: 5px; overflow: hidden;"> {style} {body} </svg>'

    # renders each component and assembles finished SVG
    def render(self):
        body = ""
        style = ""
        for i in self._render_queue:
            body += i.body()
            style += i.style()
        
        self.res.format(style=style, body=body)


    # add a component to render in a certain pos
    def add(self, component, position):
        self._render_queue.insert(position, component)

    # adds component to the end of the render queue
    def add(self, component): 
        self._render_queue.append(component)

    # removes x component from the render queue. If multiple exist, first instance is removed
    def remove(self, component): 
        self._render_queue.remove(component)

    # removes component from provided position
    def remove(self, position):
        self._render_queue.pop(position)

    # clears the queue
    def clear(self):
        self._render_queue = []


class Component():
    def __init__(self, x: int, y: int, anim_type: int, value: str, colour: str, fontsize: int):
        self.x = x
        self.y = y
        self.anim_type = anim_type
        self.value = value
        self.colour = colour
        self.fontsize = fontsize

    def body(self):
        return ""
