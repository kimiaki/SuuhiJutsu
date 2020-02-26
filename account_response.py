# -*- coding: utf-8 -*-

class Response:
    dic={"会社概要":"COMPANY",
         "事業内容":"SERVICE",
         "採用情報":"CAREER",
         "コマンド":"COMMAND",
         "おはよう":"5",
         "こんにちは":"5",
         "こんばんは":"5",
         "こんにちわ":"6",
         "こんばんわ":"6"
         }
    count=0
    
    def getResponse(self,text):
        if self.count >= 4:
            self.count = 0
        self.count += 1
        for _dic in self.dic:
            if _dic == text:
                return self.dic[text]
        return str(self.count)