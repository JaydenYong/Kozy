import webbrowser as wb
import os,atexit

class App():
    def __init__(self,filename="main"):
        self.filename = filename + ".html"
        self.writeHTML("<html>\n\t<body>\n\t\n</body>\n</html>")

        atexit.register(self.delFile())
    
    def run(self):
        wb.open(self.filename)
        
    def delFile(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            raise FileExistsError(f"{self.filename} does not exist.")
    
    def writeHTML(self,content):
        with open(self.filename,"w") as html_file:
            html_file.write(content)
    
    def Header(self,size,content):
        pass

my_app = App()

print("lol")
