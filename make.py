import json
import requests
import pprint
import wx
import pyperclip
import webbrowser

api_key = 'v^1.1#i^1#I^3#r^0#f^0#p^1#t^H4sIAAAAAAAAAOVYa2wUVRTu9kVIaYkBlTQQtoONEd3ZO4/d2R27qwul7Vr6oLsUWiXkzsyd7bC7M5OZu21XoynlFTXxbTAISYOJkRiIiELUECJE/hj1ByQS4w9ATUr90YhRIonine1SthV5dQ1N3D+bOffcc7/zne/ce2fAUOXc5dtbtl+qds0pHRkCQ6UuF1MF5lZWPFxTVlpbUQIKHFwjQw8MlQ+XjTbYMJ0yxS5km4ZuI/dgOqXbYs4YojKWLhrQ1mxRh2lki1gWY5G21SJLA9G0DGzIRopyRxtDlF/1A8bnD3BSQFH8kkqs+tWYcSNEKUggHirrR5IMFMSScdvOoKhuY6jjEMUCFngA72FBnBFEnhEZgRYY0Eu5u5Fla4ZOXGhAhXNwxdxcqwDrjaFC20YWJkGocDTSFOuIRBtXtccbvAWxwnkeYhjijD31aaWhIHc3TGXQjZexc95iLCPLyLYpb3hihalBxchVMHcAf4JqwAZZIAdYBXIBIYiKQmWTYaUhvjEOx6IpHjXnKiIdazh7M0YJG9ImJOP8UzsJEW10O39rMjClqRqyQtSqFZGeSGcnFW4x9ISVifV50jCJPJ1djR4owKCqKj7OgySFZTiVzy8yESlP8bRVVhq6ojmE2e52A69ABDGazgtXwAtx6tA7rIiKHTSFfsGr/AG+1ynoRAUzuE93aorShAR37vHm7E/OxtjSpAxGkxGmD+ToCVHQNDWFmj6Y02FeOoN2iOrD2BS93oGBAXqAow0r4WUBYLzr21bH5D6UhlTe1+n1QVu7+QSPlktFJroi/iLOmgTLINEpAaAnqDDPMMAXyPM+FVZ4uvUfhoKcvVO7oVjdAVk+yAHWz0HE+gSZL0Z3hPMC9To4kASzRJ9WEmEzBWXkkYnOMmlkaYrI+VSWC6jIo/iDqocnyvVIPsXvYVSEAEKSJAcD/5cmuVWZx5BsIVw0nRdF41HEIwk1t6so2x15mu/k1vZAOe7ztq5Hq3ihL9G6rqd3ndDNtbTyoVvthOsnLxsm6jRSmpwtIgNOrxeBBc5SOqGFszGUShHDjBK1nURnV5Gd+TYJAE2Ndpqalo2014BkN3dMG3OIZ5RzxDSj6XQGQymFosXbye/CLn7d9DRyx5lVOZH6TRRSUyYuJ3SumrTdL9MWso2MRe5ldIdzXseNJNLJDogtI5VCVjcz40Lfrfo6vf4vfNzGQXFneRf3hjJbdC2nNCKfjbMts/+8mhqcZacw4wsIPOB5QZhRXitz9YxnZ9v502LYGCm3c5EuF27xKu2d+lIfLsn9mGHXx2DYdbDU5QJeUM8sA3WVZWvLy+bV2hpGtAZV2tYSOnlXtRCdRFkTalZppctcC8fqCz4jjGwAiyY/JMwtY6oKviqAxddGKpj591cTSngWMALpS6EXLLs2Ws7cV75wPPr728/trfqw7evnx6TPXx+c98a2H0H1pJPLVVFSPuwqaR69uDl4sm4T3vHXJ6O7dowdXNGUMM7ey2XooHx+je/Qkx0njp5v6d//4uM0u2Tr/rHEyOkthxTp4qXYhfbd4VeePfVbw6vVoKvVHVvELm55LLq05WjrPsa9sOf9sfHvthwZu2LWnfSlNjSUXD7w2i8LdlZF/zy1OHrPuhPLjiyoTF5ecm5/4zff1tX8cHxjZn3VU8lKqXnfT3vaa/q3NFmHYdeVL7eBN7d7dx1/b/mj8dMP7AnVf7C7i66cv3fpgWRQ+uitJ/DhPT8v39HevXX85YEH5/Q/c+bymY62pi/Kjp2rGTU/pTzaVxfe9TXve+FYbSt3snbwnb31m399pOLsH2WfpV/6Pr6zdfyhifL9DXOQYZLgEQAA'


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title='Make', size=(800, 600))

        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label='Item:', pos=(10, 10))
        self.ans1 = wx.TextCtrl(self.panel, pos=(80, 8), size=(120, 24))

        wx.StaticText(self.panel, label='Condition:', pos=(10, 40))
        self.ans2 = wx.Choice(self.panel, choices=['new', 'used', 'whatever'], pos=(80, 38), size=(90, 24))

        search_btn = wx.Button(self.panel, label='Search', pos=(80, 70), size=(60, 24))
        search_btn.Bind(wx.EVT_BUTTON, self.on_press_1)

        self.results = [None] * 10
        for i in range(10):
            self.results[i] = wx.StaticText(self.panel, pos=(10, 100 + 15 * i))

        self.ans3 = wx.TextCtrl(self.panel, size=(0, 0))
        self.ans4 = wx.TextCtrl(self.panel, size=(0, 0))
        self.price = wx.StaticText(self.panel, pos=(290, 270))

        self.ans5 = wx.TextCtrl(self.panel, size=(0, 0))
        self.ans6 = wx.Choice(self.panel)
        self.ans6.Hide()
        self.ans7 = wx.TextCtrl(self.panel, size=(0, 0))

        fire = (wx.Image('fire_1f525.png', wx.BITMAP_TYPE_ANY).Rescale(30,30)).ConvertToBitmap()
        self.fire1 = wx.StaticBitmap(self.panel, bitmap=fire, pos=(240, 350))
        self.fire2 = wx.StaticBitmap(self.panel, bitmap=fire, pos=(270, 350))
        self.fire3 = wx.StaticBitmap(self.panel, bitmap=fire, pos=(300, 350))
        self.fire1.Hide()
        self.fire2.Hide()
        self.fire3.Hide()

        self.Show()

    def on_press_1(self, event):
        ans1_value = self.ans1.GetValue()
        if ans1_value:
            url = 'https://api.ebay.com/buy/browse/v1/item_summary/search?q=' \
                  + '+'.join(ans1_value.split()) \
                  + '&limit=10'

            ans2_value = self.ans2.GetStringSelection()
            if ans2_value == 'new':
                url += '&filter=conditions:{NEW}'
            elif ans2_value == 'used':
                url += '&filter=conditions:{USED}'
            else:
                url += '&filter=conditions:{NEW|USED}'

            response = requests.get(url, headers={'Authorization': 'Bearer ' + api_key})
            response.raise_for_status()
            jsonData = json.loads(response.text)
            # pprint.pprint(jsonData)

            itemSummaries = jsonData['itemSummaries']
            i = 0
            for itemSummary in itemSummaries:
                self.results[i].SetLabel(itemSummary['price']['currency'] + ' '
                                         + itemSummary['price']['value'] + ', '
                                         + itemSummary['condition'] + ', '
                                         + itemSummary['title'])
                i = i + 1

            wx.StaticText(self.panel, label='$', pos=(10, 270))
            self.ans3 = wx.TextCtrl(self.panel, pos=(20, 268), size=(60, 24))
            wx.StaticText(self.panel, label='with', pos=(85, 270))
            self.ans4 = wx.TextCtrl(self.panel, pos=(120, 268), size=(30, 24), style=wx.TE_RIGHT)
            wx.StaticText(self.panel, label='% off discount', pos=(150, 270), size=(60, 24))
            self.price.SetLabel('$')
            equal_btn = wx.Button(self.panel, label='=', pos=(245, 268), size=(40, 24))
            equal_btn.Bind(wx.EVT_BUTTON, self.on_press_2)

    def on_press_2(self, event):
        an4_value = self.ans4.GetValue()
        if an4_value:
            self.price.SetLabel('$' + str(round(100 * float(self.ans3.GetValue()) * (1 - float(an4_value) / 100)) / 100))
            wx.StaticText(self.panel, label='Description:', pos=(10, 320))
            self.ans5 = wx.TextCtrl(self.panel, pos=(90, 318), size=(360, 24))
            wx.StaticText(self.panel, label='Urgency:', pos=(10, 350))
            self.ans6 = wx.Choice(self.panel, choices=['1 week', '1 month', 'more than 1 month'], pos=(90, 348), size=(90, 24))
            self.ans6.Show()
            wx.StaticText(self.panel, label='Your name:', pos=(10, 380))
            self.ans7 = wx.TextCtrl(self.panel, pos=(90, 378), size=(120, 24))
            generate_btn = wx.Button(self.panel, label='Generate Message!', pos=(10, 410), size=(150, 24))
            generate_btn.Bind(wx.EVT_BUTTON, self.on_press_3)


    def on_press_3(self, event):
        ans5_value = self.ans5.GetValue()
        ans6_value = self.ans6.GetStringSelection()
        ans7_value = self.ans7.GetValue()
        if ans5_value and ans6_value and ans7_value:
            fire = (wx.Image('fire_1f525.png', wx.BITMAP_TYPE_ANY).Rescale(30,30)).ConvertToBitmap()

            if ans6_value == '1 week':
                self.fire1.Show()
                self.fire2.Show()
                self.fire3.Show()
            elif ans6_value == '1 month':
                self.fire1.Show()
                self.fire2.Show()
                self.fire3.Hide()
            elif ans6_value == 'more':
                self.fire1.Show()
                self.fire2.Hide()
                self.fire3.Hide()

            message = wx.TextCtrl(self.panel, value='Hi! My name is ' + ans7_value + '. '
                          + 'I would like to sell the ' + self.ans1.GetValue() + '.\n'
                          + ans5_value
                          + 'I need to find a buyer in ' + ans6_value + '.', pos=(10, 440), size=(480, 48), style=wx.TE_READONLY)
            pyperclip.copy(message.GetValue())

            smile = wx.Image('grinning-face-with-smiling-eyes_1f601.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            wx.StaticBitmap(self.panel, bitmap=smile, pos=(540, 270))

            post_btn = wx.Button(self.panel, label='Post to Facebook!', pos=(10, 500), size=(150, 24))
            post_btn.Bind(wx.EVT_BUTTON, self.on_press_4)


    def on_press_4(self, event):
            webbrowser.open('https://www.facebook.com/')


def main():
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
