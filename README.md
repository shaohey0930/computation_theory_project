# A Small Advanture
A little story of a magical advanture.
## Finite State Machine(FSM)
![fsm](https://github.com/shaohey0930/computation_theory_project/blob/master/fsm.png)
## Usage
The initial state is set to `user`  
- state: **user**  
    - input: `開始`
        - state: **init**
        - Reply: "在一座寬廣的森林裡...[請選擇"冒險"或是"待在原地"]"  
        - input: `待在原地`
            - state: **nostart**  
            - Reply: "你也太廢了吧，趕快離開這裡!![請選擇"冒險"^_^]"
        - input: `冒險`
            - state: **start**
            - Reple: "四處走走看好了...[請選擇"東"或是"南"或是"西"或是"北"]"
            - input: `東`
                - state: **east**
                - Reply: "岩壁...回到原本醒來的地方[請選擇"東"或是"南"或是"西"或是"北"]"
            - input: `南`
                - state: **south**
                - Reply: "大河...回到原本醒來的地方[請選擇"東"或是"南"或是"西"或是"北"]"
            - input: `北`
                - state: **north**
                - Reply: "荊棘...回到原本醒來的地方[請選擇"東"或是"南"或是"西"或是"北"]"
            - input: `西`
                - state: **west**
                - Reply: "是出口...[請選擇"進入屋內"或是"繼續趕路"]"
                - input: `進入屋內`
                    - state: **room**
                    - Reply: "桌上有著兩個打開的盒子...[請選擇"小鑽石"或是"大石頭"]"
                    - input: `小鑽石`
                        - state: **diamond**
                        - Reply: "拿了鑽石...[請輸入"繼續前進"]"
                    - input: `大石頭`
                        - state: **rock**
                        - Reply: "拿了石頭...[請輸入"繼續前進"]"
                - input: `繼續趕路`
                    - state: **keepwalk**
                    - Reply: "出於小心決定了不進入屋內...[請輸入"繼續前進"]"
                        - input: `繼續前進`
                            - state: **crow**
                            - Reply: "走著走著，發現路旁有一隻烏鴉..."
                            - 1.if you come from **keepwalk** state: "但你身上並沒有任何東西能夠幫助到烏鴉...(BAD END)" (回到 user state)
                            - 2.if you come from **diamond** state: "鑽石太小，烏鴉還是喝不到牠想要的水。...(BAD END)" (回到 user state)
                            - 3.if you come from **rock** state: "烏鴉成功喝到了水...你趁機向牠說明...(TRUE END)" (回到 user state)
                        