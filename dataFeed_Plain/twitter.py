# API Key = "X8BEZeMhZiOv8a8ivyDFBqBvo"
# API Secret Key = "Ku285B1BDIxSyGcJnqSl0ECusOIrM1Zv6KF9gCvPRGwde3zogy"

# Elated Version
# API Key = "xLZPtS2aIdcg0BnyzZwivyn73"
# API Key Secret = "3Qy9py1lN8jo3wjuoh83QpAHnMDjkpbgXfFWmkapiIH5fuaogA"
# Bearer Token = "AAAAAAAAAAAAAAAAAAAAAJj%2FlAEAAAAApWKlNmblWPyqxB%2FhgSUF0EsAL4A%3DuoqNT6pVm9IDdk3WYLpufr6WHZV5gY17hcxnKrSoLOHrlheWnD"

import requests
hed = {'Authorization': 'Bearer ' +
       "AAAAAAAAAAAAAAAAAAAAAJj%2FlAEAAAAApWKlNmblWPyqxB%2FhgSUF0EsAL4A%3DuoqNT6pVm9IDdk3WYLpufr6WHZV5gY17hcxnKrSoLOHrlheWnD"}
params = {

    'tweet_mode': 'extended',
    'lang': 'en',
    'count': '100'
}
# response = requests.get(
#    'https://api.twitter.com/2/tweets/search/recent?query=tesla', headers=hed)
# print(response.json())

dumdata = {'data': [{'edit_history_tweet_ids': ['1614937886154964992'], 'id': '1614937886154964992', 'text': 'The latest Access Motor Stocking! https://t.co/JyR2tvqjiw Thanks to @bengti0112 @EDIMOSIP #tesla #ev'}, {'edit_history_tweet_ids': ['1614937877963767809'], 'id': '1614937877963767809', 'text': 'RT @TRUTHSEEKERS111: The truth about cobalt mining and lithium batteries - Joe Rogan &amp; Siddharth Kara Part 2.\n#BreakingNews #News #CobaltMi…'}, {'edit_history_tweet_ids': ['1614937864940261378'], 'id': '1614937864940261378', 'text': 'RT @WholeMarsBlog: If you bought a Tesla last week and now the price is $20,000 less… buy another one. \n\nThat way you can dollar cost avera…'}, {'edit_history_tweet_ids': ['1614937857176788995'], 'id': '1614937857176788995', 'text': 'RT @MoneybaII_R: Tesla store visitor:\n✴️I was looking at Zeekr, NIO, Tesla\n✴️Tesla interior too plain, smart features cannot compete w/ loc…'}, {'edit_history_tweet_ids': ['1614937821374042113'], 'id': '1614937821374042113', 'text': 'RT @filmmuhendisix: The Prestige (2006) 🎬 IMDb: 8.5\n\nFilmde, birbirine düşman 2 yetenekli sihirbazın konusu anlatılıyor. Robert, eşi Julia…'}, {'edit_history_tweet_ids': ['1614937813501505537'], 'id': '1614937813501505537', 'text': 'RT @OutofSpecDetail: A perfect 2 car solution? @Tesla @Rivian https://t.co/xYxutW4K0I'}, {
    'edit_history_tweet_ids': ['1614937781377335296'], 'id': '1614937781377335296', 'text': '@Kirk_Tesla Maybe what is reported is just one side, if we find it easy to use and save money, obviously, it is in line with our own wishes'}, {'edit_history_tweet_ids': ['1614937770970988549'], 'id': '1614937770970988549', 'text': '@RoadworkUK Debadging I like though. I have a Tesla model 3 performance and would be tempted to take the "red underline" off if ti wasn\'t for the fact I\'d still have red brake calipers and a pointlessly expensive spoiler.'}, {'edit_history_tweet_ids': ['1614937767150260224'], 'id': '1614937767150260224', 'text': 'RT @DocumentingBTC: Value of $10,000 invested 12 years ago:\n\nGold = $11,800\nS&amp;P 500 = $35,400\nGoogle = $58,000\nMicrosoft = $85,000\nApple =…'}, {'edit_history_tweet_ids': ['1614937759952830467'], 'id': '1614937759952830467', 'text': 'RT @Teslarati: Tesla exec shares thoughts on Cybertruck rivals: “I think it’s great”\nhttps://t.co/BiGamrmlex by @ResidentSponge'}], 'meta': {'newest_id': '1614937886154964992', 'oldest_id': '1614937759952830467', 'result_count': 10, 'next_token': 'b26v89c19zqg8o3fqk411gf7kz585lgbl7nvoaj111rp9'}}
dumdata = dumdata["data"]
print("Here is the data", dumdata[1]["text"])
print(len(dumdata))

dumdataList = [{'edit_history_tweet_ids': ['1614937886154964992'], 'id': '1614937886154964992', 'text': 'The latest Access Motor Stocking! https://t.co/JyR2tvqjiw Thanks to @bengti0112 @EDIMOSIP #tesla #ev'}, {'edit_history_tweet_ids': ['1614937877963767809'], 'id': '1614937877963767809', 'text': 'RT @TRUTHSEEKERS111: The truth about cobalt mining and lithium batteries - Joe Rogan &amp; Siddharth Kara Part 2.\n#BreakingNews #News #CobaltMi…'}, {'edit_history_tweet_ids': ['1614937864940261378'], 'id': '1614937864940261378', 'text': 'RT @WholeMarsBlog: If you bought a Tesla last week and now the price is $20,000 less… buy another one. \n\nThat way you can dollar cost avera…'}, {'edit_history_tweet_ids': ['1614937857176788995'], 'id': '1614937857176788995', 'text': 'RT @MoneybaII_R: Tesla store visitor:\n✴️I was looking at Zeekr, NIO, Tesla\n✴️Tesla interior too plain, smart features cannot compete w/ loc…'}, {'edit_history_tweet_ids': ['1614937821374042113'], 'id': '1614937821374042113',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'text': 'RT @filmmuhendisix: The Prestige (2006) 🎬 IMDb: 8.5\n\nFilmde, birbirine düşman 2 yetenekli sihirbazın konusu anlatılıyor. Robert, eşi Julia…'}, {'edit_history_tweet_ids': ['1614937813501505537'], 'id': '1614937813501505537', 'text': 'RT @OutofSpecDetail: A perfect 2 car solution? @Tesla @Rivian https://t.co/xYxutW4K0I'}, {'edit_history_tweet_ids': ['1614937781377335296'], 'id': '1614937781377335296', 'text': '@Kirk_Tesla Maybe what is reported is just one side, if we find it easy to use and save money, obviously, it is in line with our own wishes'}, {'edit_history_tweet_ids': ['1614937770970988549'], 'id': '1614937770970988549', 'text': '@RoadworkUK Debadging I like though. I have a Tesla model 3 performance and would be tempted to take the "red underline" off if ti wasn\'t for the fact I\'d still have red brake calipers and a pointlessly expensive spoiler.'}, {'edit_history_tweet_ids': ['1614937767150260224'], 'id': '1614937767150260224', 'text': 'RT @DocumentingBTC: Value of $10,000 invested 12 years ago:\n\nGold = $11,800\nS&amp;P 500 = $35,400\nGoogle = $58,000\nMicrosoft = $85,000\nApple =…'}, {'edit_history_tweet_ids': ['1614937759952830467'], 'id': '1614937759952830467', 'text': 'RT @Teslarati: Tesla exec shares thoughts on Cybertruck rivals: “I think it’s great”\nhttps://t.co/BiGamrmlex by @ResidentSponge'}]
