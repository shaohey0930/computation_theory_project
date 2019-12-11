from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import push_text_message
rock = 0

class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def initialization(self, event):
        text = event.message.text
        return text.lower() == "開始"

    def no_to_go(self, event):
        text = event.message.text
        return text.lower() == "待在原地"

    def start_to_go(self, event):
        text = event.message.text
        return text.lower() == "冒險"

    def is_going_to_east(self, event):
        text = event.message.text
        return text.lower() == "東"
    def is_going_to_south(self, event):
        text = event.message.text
        return text.lower() == "南"
    def is_going_to_west(self, event):
        text = event.message.text
        return text.lower() == "西"
    def is_going_to_north(self, event):
        text = event.message.text
        return text.lower() == "北"

    def go_inside_the_room(self, event):
        text = event.message.text
        return text.lower() == "進入屋內"
    def keep_walking(self, event):
        text = event.message.text
        return text.lower() == "繼續趕路"

    def pick_diamond(self, event):
        text = event.message.text
        return text.lower() == "小鑽石"
    def pick_rock(self, event):
        text = event.message.text
        return text.lower() == "大石頭"

    def meet_crow(self, event):
        text = event.message.text
        return text.lower() == "繼續前進"
############################################################################################
    def on_enter_init(self, event):
        print("I'm entering init")
        reply_token = event.reply_token
        send_text_message(reply_token, "在一座寬廣的森林裡，在一處空地上，你緩緩地醒了過來。\n\"這是哪?我怎麼會在這裡?嘶...頭好痛，發生了甚麼事?\"你邊摸著後腦杓邊自言自語。\n\"從周遭看起來應該是一座森林，我應該到處走看看嗎?\"\n[請選擇\"冒險\"或是\"待在原地\"]")

    def on_enter_nostart(self, event):
        print("decide not to go")
        reply_token = event.reply_token
        send_text_message(reply_token, "你也太廢了吧，趕快離開這裡!!\n[請選擇\"冒險\"^_^]")
        self.go_back_to_start()

    def on_enter_start(self, event):
        print("decide to go")
        reply_token = event.reply_token
        send_text_message(reply_token, "\"四處走走看好了，說不定可以走出這座森林\"你起身望向四周，發現有四條道路可以選擇。\n\"我該選哪一條呢?\"\n[請選擇\"東\"或是\"南\"或是\"西\"或是\"北\"]")

    def on_enter_east(self, event):
        print("I'm entering east")
        reply_token = event.reply_token
        send_text_message(reply_token, "\"往東走好了\"你邊說著邊往東方的道路走去。\n走到一段時間，發現道路盡頭被一道非常高的岩壁擋住，你被迫回到原本醒來的地方選擇其他的道路。\n[請選擇\"東\"或是\"南\"或是\"西\"或是\"北\"]")
        self.go_back_to_ways()
    def on_enter_south(self, event):
        print("I'm entering south")
        reply_token = event.reply_token
        send_text_message(reply_token, "\"往南走好了\"你邊說著邊往南方的道路走去。\n走到一段時間，發現道路盡頭是一條足有兩人身長的大河，且河流非常湍急，你被迫回到原本醒來的地方選擇其他的道路。\n[請選擇\"東\"或是\"南\"或是\"西\"或是\"北\"]")
        self.go_back_to_ways()
    def on_enter_north(self, event):
        print("I'm entering north")
        reply_token = event.reply_token
        send_text_message(reply_token, "\"往北走好了\"你邊說著邊往北方的道路走去。\n走到一段時間，發現道路往後的路段全被荊棘叢覆蓋，你被迫回到原本醒來的地方選擇其他的道路。\n[請選擇\"東\"或是\"南\"或是\"西\"或是\"北\"]")
        self.go_back_to_ways()
    def on_enter_west(self, event):
        print("I'm entering west")
        reply_token = event.reply_token
        send_text_message(reply_token, "\"往西走好了\"你邊說著邊往西方的道路走去。\n走到一段時間，不遠處開始有亮光浮現。\n\"是出口!!我走出森林了\"你興奮的想道。\n走出森林一段時間後，一間小屋出現在路旁。你上前朝窗戶裡面看了看，發現沒人在屋子裡。\n\"走了一段時間也有點累了，我該進去休息一下嗎?但是趁主人不在偷進別人的屋子裡好像是私闖民宅耶...\"你猶豫著\n[請選擇\"進入屋內\"或是\"繼續趕路\"]")


    def on_enter_room(self, event):
        print("enter the room")
        reply_token = event.reply_token
        send_text_message(reply_token, "\"還是進去休息一下好了，反正看這一路上都沒有人應該不會有問題。\"男子想道。")
        source_id = event.source.user_id
        push_text_message(source_id, "稍作休息之後，男子起身便欲離開，出門之前突然看到旁邊桌上有著兩個打開的盒子，男子便好奇的上前查看。\n\"是一顆小鑽石!!但另一盒卻是一顆足有拳頭大的石頭\"男子看到桌上還留有一張紙條，紙條上寫道:\n\"有緣人，你可以隨機挑走一樣物品，就當作是我留給你的鑑別禮 By屋主\"\n[請選擇\"小鑽石\"或是\"大石頭\"]")
    def on_enter_keepwalk(self, event):
        print("keep walking")
        reply_token = event.reply_token
        send_text_message(reply_token, "來到未知地方的你，出於小心決定了不進入屋內，繼續趕路。\n[請輸入\"繼續前進\"]")
        


    def on_enter_diamond(self, event):
        global rock
        print("pick diamond")
        reply_token = event.reply_token
        rock = 1
        send_text_message(reply_token, "\"當然是選擇小鑽石啊!這種好康我怎麼可以錯過\"你不做他想便順手拿了鑽石。\n神奇的是，當你拿起了鑽石後，另一個盒子就自動的關起來了。\n摸不著頭緒的你只好繼續趕路。\n[請輸入\"繼續前進\"]")
        
        
    def on_enter_rock(self, event):
        global rock
        print("keep walking")
        reply_token = event.reply_token
        rock = 2
        send_text_message(reply_token, "\"還是拿石頭好了，做人不可以太貪心\"你謹慎的選擇了石頭。\n神奇的是，當你拿起了石頭後，另一個盒子就自動的關起來了。\n摸不著頭緒的你只好繼續趕路。\n[請輸入\"繼續前進\"]")


    def on_enter_crow(self, event):
        print("meet the crow")
        reply_token = event.reply_token
        send_text_message(reply_token, "走著走著，發現路旁有一隻烏鴉帶著一瓶裝滿石頭的燒杯，同時不斷的把嘴巴往瓶口內塞，似乎想喝到裡面的水，你好奇的上前查看了一下，沒想到烏鴉竟然開口說話了。")
        source_id = event.source.user_id
        push_text_message(source_id, "\"年輕人，我好渴，如果你可以幫助我喝到裡面的水，我將滿足你一個願望。\"烏鴉向你求救。")
        if rock == 0: # don't have things on hand
            push_text_message(source_id, "但你身上並沒有任何東西能夠幫助到烏鴉，只能眼睜睜的看著烏鴉繼續乾著急著。\n烏鴉就此渴死了，而你則繼續流浪在這個世界，徘徊流浪著直到最後。")
            push_text_message(source_id, "(BAD END)\n[請輸入\"開始\"來開啟一段新的故事]")
        elif rock == 1: # got the diamond
            push_text_message(source_id, "此時的你想到了剛剛拿到的鑽石，想著這個應該可以幫助到牠，就將你拿到的鑽石丟了進去。\n沒想到鑽石太小了，丟進去竟沒有讓水位高多少，烏鴉還是喝不到牠想要的水。\n烏鴉就此渴死了，而你則繼續流浪在這個世界，徘徊流浪著直到最後。")
            push_text_message(source_id, "(BAD END)\n[請輸入\"開始\"來開啟一段新的故事]")
        else:
            push_text_message(source_id, "此時的你想到了剛剛拿到的石頭，想著這個應該可以幫助到牠，就將你拿到的石頭丟了進去。\n當石頭丟進燒杯後，燒杯的水剛剛好滿了，烏鴉成功喝到了水。\n\"年輕人，謝謝你，說吧你想要甚麼願望?\"滿足的烏鴉回過頭來向你問道。\n你趁機向牠說明想要回到家裡，烏鴉點點頭，叫了兩聲之後，你的腳下出現了魔法陣，此時的你才發現這隻烏鴉竟然會施展魔法!")
            push_text_message(source_id, "一陣頭暈目眩之後，醒來的你已經躺在家裡的床上了，剛剛的一切只不過像是夢境一般曇花一現，故事也到此結束。")
            push_text_message(source_id, "(TRUE END)\n[請輸入\"開始\"來開啟一段新的故事]")
        self.go_back_to_user()
############################################################################################
    #def on_exit_init(self):
        #print("Leaving init")

    #def on_exit_state2(self):
        #print("Leaving state2")
