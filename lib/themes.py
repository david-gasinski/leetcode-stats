import json

class Theme():
    def __init__(self, theme: str) -> None:
        self.path = './lib/json/colours.json'
        self.theme = theme
        self._loadTheme()
    
    def _loadTheme(self) -> None:
        """ Loads the colour themes from json file and appends to colours object """
        with open(self.path, 'r') as f:
            colours_dic = json.loads(f.read())
        
        theme = colours_dic[self.theme.lower()]
        for key in theme:
            setattr(self, key, theme[key])
