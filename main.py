import webbrowser as wb
import os,atexit,time

class App():
    def __init__(self,filename="main",auto_delete=False):
        self.filename = filename + ".html"
        self.auto_delete = auto_delete
        self.writeHTML("<html>\n\t<body>\n\t\n</body>\n</html>")

        if self.auto_delete == True:
            atexit.register(self.delFile)
        else:
            atexit.unregister(self.delFile)
    
    def run(self):
        wb.open(self.filename)
        
    def delFile(self):
        if os.path.exists(self.filename):
            time.sleep(5)
            os.remove(self.filename)
        else:
            raise FileExistsError(f"{self.filename} does not exist.")
    
    def writeHTML(self,content):
        with open(self.filename,"w") as html_file:
            html_file.write(content)
    
    def Header(self,size,content):
        pass