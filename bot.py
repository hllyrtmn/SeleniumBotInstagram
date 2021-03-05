from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome("E:\Dersler\Python\Bot\chromedriver.exe")
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username) #kullanici adinın girildiği alan girilmesi
   
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw) #parolanın  girildiği alan
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click() #giriş butonuna basmak
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click() # giriş bilgileri kaydedilsin mi
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click() # bildirimleri aç kapa


    def get_takip(self,kullanici):

        self.driver.get("https://www.instagram.com/explore/tags/{}/".format(kullanici))
        sleep(3)
        for i in range(0,50):                               
            for ik in range(0,2):
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[{}]/div[{}]/a/div[1]/div[2]".format((i+1),(ik+1))).click() # etiketin ilkine bas sonra alttaki etikete geç
                sleep(3)        
                                                    
                etiket = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]")
                buton = etiket.find_elements_by_class_name("sqdOP")
                butonetiket = [name.text for name in buton if name.text !='']
                # sqdOP yWX7d     _8A5w5    beğen butonu class
                #div class HbPOm _9Ytll
                sectionsec = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[2]")
                isimclass = sectionsec.find_elements_by_class_name("_8A5w5")

                print(isimclass)
                print(type(isimclass))
                
            
                print(butonetiket)
                print(type(butonetiket))

                if butonetiket[0] == 'Takip Et':
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click() #etiket açılınca takip ete bas BUNU KONTROL ET TAKİPTESİN İSE TIKLAMA
                    sleep(2)
                    # sorun_varmi = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div")
                    # sorun_var = sorun_varmi.find_elements_by_class_name("HoLwm")
                    # print(sorun_var)
                    # names = [name.text for name in sorun_var if name.text != '']
                    # print(names)
                    # sleep(5)
                    # if names[0] == 'Tamam':
                    #     self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/button[2]").click()
                    sleep(2)

                if len(isimclass) != 0:    
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button").click()
                    sleep(4)
                    sugs = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div[1]')
                    self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
                    scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div")
                    last_ht, ht = 0, 1
                    sayac = 0
                    while sayac != 30:
                        takip_mi = scroll_box.find_elements_by_class_name('sqdOP')
                        takip_isim = [name.text for name in takip_mi if name.text !='']
                        print(takip_isim)
                        for il in range (0,11):
                            if takip_isim[il] == 'Takip Et':
                                self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div[{}]/div[3]/button".format(il+1)).click()
                                sleep(10)
                                # sorunvarmi = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div")
                                # sorunvar = sorunvarmi.find_elements_by_class_name("HoLwm")
                                # print(sorunvar)
                                # namess = [name.text for name in sorunvar if name.text != '']
                                # sleep(5)
                                # if namess[0] == 'Tamam':
                                #     self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/button[2]").click()
                                sleep(2)
                                sayac += 1
                            else:
                                continue
                            sleep(3)
                        ht = self.driver.execute_script("""
                                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                                return arguments[0].scrollHeight;
                                """, scroll_box)    

                    self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
                else:
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
        #/html/body/div[5]/div/div/div[2]/div/div/div[11]
        #/html/body/div[5]/div/div/div[2]/div/div/div[1]
        # self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
        #     .click()
        # followers = self._get_names()
        # scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        # takip_mi = scroll_box.find_elements_by_class_name('sqdOP')
        # takip_isim = [name.text for name in takip_mi if name.text !='']

        # for i in range (0,100):
        
        #     if takip_isim[i] == 'Takip Et':
        #         self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button".format(i+1)).click()
        #         sleep(2)
        #     else:
        #         continue

    def _get_names(self):
        sleep(10)
        sugs = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[1]/div')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        
    def takip_ediyormu(self):
        sleep(10)
        sugs = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[1]/div')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names
    def kenditakip(self):
        self.driver.get("https://www.instagram.com/{}".format(self.username))
        sleep(2)
        
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self.takip_ediyormu()
        print(len(followers))
        
        
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
             .click()
        following = self.takip_ediyormu()
        print(len(following))
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        for i in not_following_back:
            self.driver.get("https://www.instagram.com/{}/".format(i))
            sleep(3)
                                               #/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div[2]/button
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button").click()
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
            sleep(3)
        
    def liste(self):
        self.driver.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")
        sleep(2)
        sayac = 1
        while sayac == 1:
            main_liste = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main")
            main_liste_bul = main_liste.find_elements_by_class_name("sqdOP")
            if len(main_liste_bul) != 0:
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main/button").click()
                sleep(1)
            else:
                sayac = 0
                liste_section = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main/section")
                liste_isim_bul = liste_section.find_elements_by_class_name("-utLf")
                liste_isimler = [name.text for name in liste_isim_bul if name.text != '']
                print(liste_isimler)
        return liste_isimler

    def isteksil(self, liste):
        for i in liste:
            self.driver.get("https://www.instagram.com/{}/".format(i))
            sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/button").click()
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
            sleep(2)

        
    
        




print("\n-----------------")
user = input("Kullanıcı Adınız: ")
password = input("Parolanız: ")
print( "-----------------\n")
print("1. Otomatik Takip\n2.Takip Etmeyenleri Çıkar\n3.İstekleri Kaldır\n")
secim = input("Seçiminiz: ")
if(secim == '1'):
    kullanici = input("Etiket Giriniz: ")
    my_bot = InstaBot(user, password)
    my_bot.get_takip(kullanici)
elif(secim == '2'):
    my_bot = InstaBot(user, password)
    my_bot.kenditakip()
elif(secim == '3'):
    my_bot = InstaBot(user,password)
    abc = my_bot.liste()
    my_bot.isteksil(abc)
else:
    print("Hatalı Giriş")




# /html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[{}]/a/div[1]/div[2]  #tarim dan sonra çıkan resimler
# /html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div[1]/div[2]

# /html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button resime tıklanınca çıkış butonu

# /html/body/div[4]/div[2]/div/article/div[3]/section[2]/div görüntülenme

# /html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button beğenme