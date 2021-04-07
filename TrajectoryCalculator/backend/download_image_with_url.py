




import requests,os, random, string


# a simple script to download images using the requests library
# it wil automatically save  images on  'Desktop/Image downloads

class ImageDownloader():
    
    def __init__(self):
        self.user = os.getlogin()
        dest = f"C:/Users/{self.user}/Desktop/Image downloads/"
        self.check_dir(dest)
        self.destination_dir = dest
        self.running = True
        
    
    def check_dir(self, directory):
        if  os.path.isdir(directory) == False:
            try:
                os.makedirs(directory)
            except:
                print('\nfailed to create !!')
                
    def get_random_name(self):
        random_name =  random.choices(string.ascii_lowercase, k= 5)
        new_name = ''
        for char  in random_name:
            new_name = new_name.join(char)
        new_name = new_name + 'jpg'
        return new_name        
    def download_with_url(self, url, directory = ''):
        if directory == '':
            directory = self.destination_dir
        response = requests.get(url, stream = True)
        if response.status_code == 200:
            # giving a random name to th eimages
           
                
            random_name = self.get_random_name()
            name = os.path.join(self.destination_dir , random_name)
            with open(name, 'wb') as f:
                try:
                    f.write(response.content)
                    print(url,'image downloaded\n')
                except:
                    print('image not downloaded .....',url)
         
    def download_multiple_urls(self, list_of_urls):
        # download a list of urls
        for url in list_of_urls:
            self.download_with_url(url)
            
            
        
               
                
                
    def run_interface(self):
        print("""
    
    
    1  .  Download  a single images
    2  .  Download multiple images
    3  .  exit
    
    """)
        while self.running :
            choice = input(" _> ")
            if choice == '1':
               
               
                print('enter image url \n')
                url  = input("_> ")
                self.download_with_url(url)
                
            elif choice == '2':
                print('enter the urls and enter  OK to start download\n')
                multi_mode = True
                while multi_mode:
                    urls = []
                    inp = input('url >')
                    if inp == 'OK':
                        multi_mode = False
                        self.download_multiple_urls(urls)
                        
                    else:
                        urls.append(inp)
            elif choice == "3":
                self.running = False
                    
                



if __name__ == '__main__':
    ImageDownloader().run_interface()
    