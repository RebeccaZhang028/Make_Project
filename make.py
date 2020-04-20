import json
import requests
import pprint
import wx

api_key = 'v^1.1#i^1#p^1#I^3#r^0#f^0#t^H4sIAAAAAAAAAOVYfWwURRTvXb9oSkUTooYQc24hRuD2Zr96dwt3eLTFXmivR+9oaVHr7O5su/T2I7tztIegTaVNADEq8Q/9AxuDxsQQQ6JRCYlRUSMIKMQYq6KExBCVPzAElBh1d3uUa0W+eoYm3j+XefPmze/93nszbwcMVlQtGmkauVDjqfSODoJBr8dDVYOqivLFt5V655WXgAIFz+jggsGyodLTyyyoZgy+DVmGrlnIN6BmNIt3hREia2q8Di3F4jWoIovHIp+KtTTzNAl4w9SxLuoZwhdviBCCBCWGo4IQMUCmw6wt1S7ZTOv2PBUU6+QwEEJ1siBTyJ63rCyKaxaGGo4QNKCBH7B+GqQpjmcBz3EkzYEuwteOTEvRNVuFBETUhcu7a80CrFeHCi0Lmdg2QkTjsZWp1li8oTGRXhYosBXN85DCEGetyaN6XUK+dpjJoqtvY7nafCorisiyiEB0fIfJRvnYJTA3Ad+lWg7RkozYsBQKMTTNMkWhcqVuqhBfHYcjUSS/7KrySMMKzl2LUZsNYT0ScX6UsE3EG3zO3+oszCiygswI0bgi1hlLJolok671mNlUr1+FfcifbGvwwyAMy7LEMX4kSDTFyGx+k3FLeYqn7FKva5LiEGb5EjpegWzEaCovTAEvtlKr1mrGZOygKdQLXuKP5bqcgI5HMIt7NSemSLVJ8LnDa7M/sRpjUxGyGE1YmDrh0hMhoGEoEjF10s3DfOoMWBGiF2ODDwT6+/vJfobUzZ4ADQAVWNvSnBJ7kQqJvK5T6wOWcu0FfsV1RbRL1Nbncc6wsQzYeWoD0HqIKEtRgAvleZ8MKzpV+g9Bgc+BydVQrOoQAF3HCaLAimIQMnV0Maojmk/QgIMDCTBn56fZh7CRgSLyi3aeZVVkKhLPcDLNhGTkl+rCsp+1M9cvcFKdn5IRAggJghgO/V+K5HrTPIVEE+Gi5XlRcjyOWCSgBxMyyrXHNrJJZk0nFNNcYNVa1MgGe3tWdXR2dQTbmaZVbOR6K+HKzou6gZJ6RhFzRWTAqfUisMCYUhKaOJdCmYwtmJajluPozAqys96yDUBDIZ2iJkVdDejQPs0dUbeLeFo+xwwjrqpZDIUMihfvJL8Fp/gV3VPsHmdG+WTHbzyQijTenJBuNElrg0iayNKzpt2Xka3OfZ3W+5Bmn4DY1DMZZLZT0w70rYqvU+v/wscNXBQ353dxO5SZktdiRrHTp3umefafR1OBM+wWprhQkAkHaY6bll/1bjzTuZl2/zTpFkbSjTTSZcHrbKUDkz/qoyXujxryvAWGPHu9Hg8IgIVULbi3onRNWenseZaCEalAmbSUHs3+VjUR2YdyBlRMb4XHWAN/WljwjDD6MLh74iGhqpSqLnhVAPMvz5RTc+6qsSlhaUBxLOC4LlB7ebaMurNs7uHTw7tPR5Qtb7RlX/5s1ligeng2BDUTSh5PeUnZkKfknj1rd/arL1V9c2TgY7xaP7svtK5+9cEjRs0Px3954fVdiUW3f760au6Zv+Qd6T+PPjqqd82Szs0ZYBacnx979XxzQ/KUuR629m7fFO7fdbjqlecDy4N3hOjWyuH7n12UpE/et2vfllOPbX7Kgy488vPb/sNfbjr2wUFqdBse2rpsibJn+YGNw32JsbNN69oe/6Ll+ANfkbTS+U638eaL9St276gdOdRY07Y0c+6ct8Nb+ekfjR+eVD45+F3Hmc2JX0fG3j2afO/CiVnb9/72+5PPtX+05P31TxxSN/Tsr3joQKKymxa+rQ0d47Lyjxt2HgtXbGvZ2vf9Rq98sXnP/q/3jp14+qI6WO17bWjxM+Ph+xvaeNgQ4BEAAA=='


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
        self.ans6 = wx.TextCtrl(self.panel, size=(0, 0))

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
            wx.StaticText(self.panel, label='Your name:', pos=(10, 350))
            self.ans6 = wx.TextCtrl(self.panel, pos=(90, 348), size=(120, 24))
            generate_btn = wx.Button(self.panel, label='Generate Message!', pos=(10, 380), size=(150, 24))
            generate_btn.Bind(wx.EVT_BUTTON, self.on_press_3)


    def on_press_3(self, event):
        ans5_value = self.ans5.GetValue()
        ans6_value = self.ans6.GetValue()
        if ans5_value and ans6_value:
            wx.TextCtrl(self.panel, value='Hi! My name is ' + ans6_value + '. '
                          + 'I would like to sell the ' + self.ans1.GetValue() + '. '
                          + ans5_value, pos=(10, 410), size=(480, 24))

        png = wx.Image('grinning-face-with-smiling-eyes_1f601.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self.panel, bitmap=png, pos=(540, 350))


def main():
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
