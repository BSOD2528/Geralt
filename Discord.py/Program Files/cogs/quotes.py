from os import name
import discord
import json
import random
import datetime
import asyncio
from discord.ext import commands

class Quotes(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
    emote = json.load(open('D:\AV\PC\Coding\Discord Bot\Geralt\Discord.py\Program Files\emote.json'))

#---pattani---#
    @commands.command(name = 'pieace', help = 'Enjoy some piease')
    async def pieace(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        peace = ['Pieace Homies',
                 'Be calm and pieacefull :pray: Things will go your way',
                 '<:jp:879708834820661270>',
                 'https://en.wikipedia.org/wiki/Pea',
                 'Pieacefullness is something everyone requires in their lives. On the contrary, no one has it.',
                 'https://www.google.com/search?q=peas&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjPsbuD2cnyAhXFmeYKHV_FAzgQ_AUoAXoECAEQAw&biw=1366&bih=649',
                 'Jai Pattani FOR LIFE! SAY ITT!! Otherwise <:linuskill:886606006761717760><:linuskill:886606006761717760><:linuskill:886606006761717760>',
                 'Everyone generally say " Leave me in Peace "; while I say Leave me in pieace <:jp:879708834820661270>',
                 'PIEACE = PEACE + PIECE --> Its no where related to peas, but yeah it just popped up.',
                 'You know Hitler hated Peas <:broo:877044811402735638>',
                 'If you say peace ever again, your <:linuskill:886606006761717760>',
                 '<:jp2:879720666167918633>']
        emb = discord.Embed(
            title = 'Pieace',
            description = f'{ctx.message.author.mention} {random.choice(peace)}',
            color = ctx.author.color)
        await ctx.reply(embed = emb)

#---bts quotes---#
    @commands.command(aliases = ['bq'], help = 'Motivation !!', brief = 'Get motivated with the best quotes from BTS!')
    async def btsq(self, ctx):
        quote = ['Hark work will never betray you - KIM TAEHYUNG',
                 'Go on your path, even if you live only for a day - JIMIN',
                 'Take off the mask and face yourself - BTS',
                 'Even if you are not perfect, you are defenitely a limmited edition. - KIM NAMJOON',
                 'You rise when I go down, because Im the sun and your the moon - MIN YOONGI - GI',
                 'If you want to love others, I think you should love yourself first. – RM',
                 'I have a big heart full of love, so please take it all.  – V',
                 'When we don’t have a boyfriend or girlfriend, we always say, ‘Oh, I’m so lonely. I want a date,’ or something like that. But I think the biggest love we’re all searching for is the love for one’s self. – RM',
                 'Those who want to look more youthful should live life with a young heart. – JIN',
                 'I have come to love myself for who I am, for who I was, and for who I hope to become. — RM',
                 'We’re trying to say that if you, in love, when you’re not true to yourself, the love won’t last. Because love is complex, and we always have the dark sides and the sad sides. – RM',
                 'Effort makes you. You will regret someday if you don’t do your best now. Don’t think it’s too late but keep working on it. It takes time, but there’s nothing that gets worse due to practicing. So practice. You may get depressed, but it’s evidence that you are doing good. – JUNGKOOK',
                 'In the middle of the road, in the moment you want to give up, shout out even louder: So what? - BTS',
                 'Don’t be trapped in someone else’s dream. – V',
                 'Your presence can give happiness. I hope you remember that. – JIN',
                 'Life is a sculpture that you cast as you make mistakes and learn from them. — RM',
                 'If you think you’re going to crash, step on the pedal harder. – SUGA, NEVERMIND',
                 'Erase all sad memories. Hold each other’s hands and smile. — BTS 2! 3!',
                 'To lose your path is the way to find that path. — BTS, LOST',
                 'Go on your path, even if you live for a day. Do something. Put away your weakness. – BTS, NO MORE DREAMS',
                 'If you can’t fly, then run. Today we will survive. – BTS, NOT TODAY',
                 'Whatever, big or small, you are you after all. – BTS, PARADISE',
                 'The morning will come again. No darkness, no season is eternal. – BTS, SRPING DAY',
                 'I’m like a surfer, first you just paddle and fall off the board but as time goes by you can stand up on the bigger waves.” – RM',
                 'Living without passion is like being dead. - JUNGKOOK',
                 'Humans seem to be programmed to think of ambivalent feelings at the same time. That is the driving force behind human beings: to be the warrant of all things and to control other worlds. – RM',
                 'Even if it’s a road of thorns, we still run. – SUGA, NEVER MIND',
                 'They say people live to be happy. If you actually think about what happiness is, it’s nothing much. When you get to eat ramen after feeling really, really hungry, that’s happiness. – RM',
                 'It’s all right to not have a dream, if you have moments where you feel happiness for a while. —  BTS, PARADISE',
                 'Not so perfect, but so beautiful — JIN, EPIPHANY',
                 'The dawn right before the sun rises is the darkest. – BTS, TOMORROW',
                 'I’m becoming weird. You can’t go to the peak by being normal, baby. – BTS, BOYZ WITH FUN',
                 'Isn’t a man someone who doesn’t care about what others think? A man does whatever he wants. – JUNGKOOK',
                 'I believe in myself. My back hurts in order to let my wings sprout. — BTS, INTERLUDE: WINGS',
                 'I’m always afraid of making mistakes. I think I was born with that. – RM',
                 'When I perform my role well, I feel proud. – RM',
                 'Every moment is memorable to me. – SUGA',
                 'Popularity is a bubble. It’s a mountain: you can go up really hard but walk down really fast. – RM',
                 'I think BTS is able to shine because we have fans. – SUGA',
                 'In general, what fans talk about and think about become a very important source of inspiration to us, because we want to write something that’s real to people, especially those who listen to BTS music. – SUGA',
                 'If you don’t work hard, their won’t be a good result. – J-HOPE',
                 'Music transcends language. BTS communicates with our fans by staying true to ourselves and believing in music every day. – RM',
                 'There are a lot of things that we want to show people, and if you try to show everything about us in a single album, it’s a burden for us – and it’s a lot for people to handle and accept. – JUHNGKOOK',
                 'I try not to be influenced by success or popularity. – SUGA',
                 'If I had a chance to improve every aspect of myself, then I would work hard to make it happen rather than just sitting idle – JUNGKOOK',
                 'Good music will always be recognized in the end. – SUGA',
                 'It’s my official role to represent BTS to the world, and it’s been a chance for me to mature as a person, but behind the scenes, I’m just one of seven members, and I’m inspired by the others all the time. – RM',
                 'We do make sure that one person doesn’t stand out. But then, we are really unique. We all have our style, so I think we all stand out. We each have our own roles and positions in the band, and then we work together to make sure we all try hard for the Army. – Jungkook',
                 'I get free life lessons from J-Hope and Jimin; sometimes it’s like they’re 10 years older than me. – RM',
                 'Jin used to be an ordinary guy in the team, but he’s the mood maker now. He’s the most wicked and funniest of all. No one in BTS is normal, though, come to think of it. – JUNGKOOK',
                 'We do make sure that one person doesn’t stand out. But then, we are really unique. We all have our style, so I think we all stand out. We each have our own roles and positions in the band, and then we work together to make sure we all try hard for the Army. – JUNGKOOK',
                 'I taught myself English. My English teacher was the sitcom ‘Friends.’ Back in the days when I was, like, 15, 14, it was like a syndrome for Korean parents to make their kids watch ‘Friends.’ I thought I was a victim at that time, but now I’m the lucky one. – RM',
                 'I first paid attention to fashion when I was around 15, but I don’t really care much about it these days. – SUGA',
                 'I was an underground rapper and only 16 years old, a freshman at high school. Bang thought I had potential as a rapper and lyricist, and we went from there. Then Suga joined us. – RM',
                 'When I was younger, I thought that everything would just come to me eventually, but now I see I have to take the initiative and practice to improve myself. – JUNGKOOK',
                 'Love myself, love yourself, peace. ― MIN YOONGI-G',
                 'When something is delicious. It’s zero calories. – JIN',
                 'Find your name, find your voice by speaking yourself. - KIM NAMJOON',
                 'Even when this rain stops, when clouds go away, I stand here, just the same. – J-HOPE',
                 'Thank you for accepting us. The 7 boys from Korea who sing in Korean. - KIM NAMJOON',
                 'Life is tough, and things don’t always work out well, but we should be brave and go on with our lives. – SUGA',
                 'Those who don’t have a dream, it’s okay, it’s okay if you don’t have a dream. You just have to be happy. - MIN YOONGI-G',
                 'A warm smile is the universal language of kindness. - J-HOPE',
                 'I believe that there’s no improvement if you have an inferiority complex and victim mentality. - KIM NAMJOON',
                 'Even if I’m a little hurt it’s okay. - JIMIN',
                 'Teamwork makes the dream work. - BTS',
                 'Once your heart is moved, it will develop to something better and positive. – JIMIN',
                 'Purple is the last colour of the rainbow colours. So means I will trust and love you for a long time. - KIM TAEHYUNG',
                 'The music helped me sympathize with our young generation and also empathize with them. I’d like to create and write more music that represents them. – J-HOPE',
                 'With you I’mma feel rich. - PARK JIMIN',
                 'Emotions are so different in every situation and every moment, so I think to agonize every moment is what life is. – SUGA',
                 'We were too young and immature to give up, you idiot - MING YOONGI',
                 'So please don’t leave me you got the best of me. – J-HOPE',
                 'I want to eat and play. I want to tear my uniform. ― JUNG HOSEOK',
                 'Know that the pain will pass. And when it does you will be stronger. - JIMIN',
                 'If I want to die, I’ll strive to live as much as I want to die – MOONCHILD – RM',
                 'It’s okay, come on when I say one, two, three, forget it / Erase all sad memories – 2!3! ( HOPING FOR MORE GOOD DAYS )',
                 'Go your own way / Even if you live a day / Do something / Put weakness away – NO MORE DREAM',
                 'All the dreamers / Put your hands up / Throw your worries away – JUMP',
                 'We must believe only in ourselves – LOVE MAZE',
                 'Dream, you will fully bloom / After all the hardships / So Far Away – AGUST D',
                 'I’m diamond, you know I glow up – DYNAMITE',
                 'Yes we’re livin’ and dyin’ / At the same time / But you can open your eyes for now – 4 O’CLOCK',
                 'Don’t ever be scared / Whatever people say, you’re okay – 21st CENTURY GIRLS',
                 'I reject rejection – DOPE',
                 'Can’t hold me down ‘cuz you know I’m a fighter – ON',
                 'IN the dark dawn, spreading trembling wings / Keep on shining make it brighter than a spotlight – DREAM GLOW',
                 'You can’t stop me lovin’ myself – IDOL',
                 'If you try to damage me with simple words like that / I only become stronger – CYPHER PT. 3 : KILLER',
                 'Forever we are young / Even when I fall and hurt myself / I keep running towards my dream – EPILOGUE : YOUNG FOREVER',
                 'In the dark night, don’t be lonely / Like the stars, we shine / Don’t disappear, because you’re a great existence / Let us shine – MIKROKOSMOMS',
                 'So what / Don’t stop and worry yourself / It’s good for nothing / Let go – SO WHAT?',
                 'You shine in this pitch darkness / That is the butterfly effect – BUTTERFLY',
                 'It’s okay to shed the tears / But don’t you tear yourself – MOONCHILD - RM',
                 'You can’t just come into someone’s life, make them feel special, and then leave. – TAEHYUNG',
                 'If you can’t respect, don’t even open your mouth. – KIM NAMJOON']
        emb = discord.Embed(
            title = 'FAMOUS QUOTES FROM BTS',
            description = f'{ctx.message.author.mention} {random.choice(quote)}',
            color = ctx.author.color)
        emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.reply(embed = emb)
    @btsq.error
    async def quotes_error(self, ctx, error):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        emb = discord.Embed(
            title = 'Syntax Error',
            description = '{ctx.message.author.mention} its `gquotes` or `gbtsi`.',
            color = ctx.author.color)
        await ctx.reply(embed = emb)
    
#---anime quotes---#
    @commands.command(aliases = ['aq'], help = 'Love Anime?', brief = 'Relate to the best anime quotes out there!')
    async def animeq(self, ctx):
        quote = ['The world isn’t perfect. But it’s there for us, doing the best it can, that’s what makes it so damn beautiful. – Roy Mustang',
                 'Knowing you’re different is only the beginning. If you accept these differences you’ll be able to get past them and grow even closer. – Miss Kobayashi',
                 'Even if I die, you keep living okay? Live to see the end of this world, and to see why it was born. Live to see why a weak girl like me ended up here… And the reason you and I met. – Sachi',
                 'We each need to find our own inspiration. Sometimes, it is not easy. – Kiky’s Delivery Service.',
                 'Giving up is what kills people. – Hellsing',
                 'No matter how deep the night, it always turns to day, eventually. – One Piece',
                 'Sometime, its necessary to do unncesarry things. - Kanade Jinguuji',
                 'How can you move forward when you keep regretting the past? – Fullmetal Alchemist',
                 'Don’t give up, there’s no shame in falling down! The true shame is to not stand up again! – Shintaro Midorima',
                 'It may be hard right now but you must silent those thoughts. Stop counting those things you have lost, what is gone is gone. So ask yourself, what is there that still remains to you. – One Piece',
                 'To know sorrow is not terrifying. What is terrifying is to know you can’t go back to happiness you could have. – Matsumoto Rangiku',
                 'It’s just pathetic to give up on something before you even give it a shot. – Reiko Mikami ',
                 'If you don’t take risks, you can’t create a future. – Monkey D. Luffy',
                 'If you win, you live. If you lose, you die. If you don’t fight, you can’t win. – Eren Yaeger',
                 'People’s lives don’t end when they die, it ends when they lose faith. – Itachi Uchiha',
                 'Pretty words arent always true, and true words arent always pretty. - Kazuma',
                 'We are all like fireworks: we climb, we shine and always go our separate ways and become further apart. But even when that time comes, let’s not disappear like a firework and continue to shine.. forever. – Hitsugaya Toshiro',
                 'Fear is not evil. It tells you what weakness is. And once you know your weakness, you can become stronger as well as kinder. – Gildarts Clive',
                 'I want you to be happy. I want you to laugh a lot. I don’t know what exactly I’ll be able to do for you, but I’ll always be by your side. – Kagome',
                 'If you don’t like your destiny, don’t accept it. Instead, have the courage to change it the way you want it to be! – Uzumaki Naruto',
                 'Those who stand at the top determine what’s wrong and what’s right! This very place is neutral ground! Justice will prevail, you say? But of course, it will! Whoever wins this war becomes justice! – Don Quixote Doflamingo',
                 'I just appreciate silence in a world that never stops talking. - Nico Edogawa',
                 'Whatever you lose, you’ll find it again. But what you throw away you’ll never get back. – Kenshin Himura',
                 'When you give up, that’s when the game ends. – Mitsuyoshi Anzai',
                 'Fear is freedom! Subjugation is liberation! The contradiction is the truth! Those are the facts of this world! And you will all surrender to them, you pigs in human clothing! – Satsuki Kiryuuin',
                 'I am the hope of the universe. I am the answer to all living things that cry out for peace. I am the protector of the innocent. I am the light in the darkness. I am the truth. Ally to good! Nightmare to you! – Son Goku',
                 'Thinking you’re no–good and worthless is the worst thing you can do – Nobito',
                 'You hear, but are you listening? You exit, but are you living? You look, but do you see? - Kairos',
                 'All we can do is live until the day we die. Control what we can…and fly free. – Deneil Young',
                 'Religion, ideology, resources, land, spite, love or just because… No matter how pathetic the reason, it’s enough to start a war. War will never cease to exist… reasons can be thought up after the fact… Human nature pursues strife. – Paine',
                 'Forgetting is like a wound. The wound may heal, but it has already left a scar. – Monkey D. Luffy',
                 'People who can’t throw something important away can never hope to change anything. – Armin Arlelt',
                 'Giving up kills people. When people reject giving up… they finally win the right to transcend humanity. – Alucard',
                 'Weaklings will stay weak forever. But weakness is not evil since human beings are weak creatures, to begin with. Alone, you feel nothing but insecurity; that’s why we form guilds, that’s why we have friends. We walk together in order to live a strong life. The clumsy ones will walk into more walls than the others, and it may also take them longer to get there. If you believe in tomorrow and put yourself out there, you can naturally obtain your strength. That’s how you will be able to smile and live strong. – Makarov Dreyar',
                 'If you don’t share someone’s pain, you can never understand them. – Nagato',
                 'I’m not stupid. I’m just too lazy to show how smart I am. – Oreki Houtarou',
                 'Knowing you’re different is only the beginning. If you accept these differences you’ll be able to get past them and grow even closer. – Miss Kobayashi',
                 'To know sorrow is not terrifying. What is terrifying is to know you can’t go back to happiness you could have. – Matsumoto Rangiku',
                 'The true measure of a shinobi is not how he lives but how he dies. It’s not what they do in life but what they did before dying that proves their worth. – Jiraiya',
                 'Fake people have an image to maintain. Real people just don’t care. – Hachiman Hikigaya',
                 'We don’t have to know what tomorrow holds! That’s why we can live for everything we’re worth today! – Natsu Dragneel',
                 'Why should I apologize for being a monster? Has anyone ever apologized for turning me into one? – Juuzou Suzuya',
                 'No single thing is perfect by itself. That’s why we’re born to attract other things to make up for what we lack. I think we start walking in the right direction only after we start getting our counterparts besides us. – Itachi Uchiha',
                 'Can you hear the silence? Can you see the dark? Can you fix the broken? Can you feel my heart? - Karunase',
                 'A castle that vanishes at the first gust of wind is worthless. – Kill la Kill',
                 'Every journey begins with a single step. We just have to have patience. – Milly Thompson',
                 'I’ll leave tomorrow’s problems to tomorrow’s me. – Saitama',
                 'I don’t want to conquer anything. I just think that the guy with the most freedom in this ocean is the Pirate King! – Monkey D. Luffy',
                 'Hard work betrays none, but dreams betray many. – Hachiman Hikigaya',
                 'If nobody cares to accept you and wants you in this world, accept yourself and you will see that you don’t need them and their selfish ideas. – Alibaba Saluja',
                 'Being lonely is more painful then getting hurt. – Monkey D. Luffy',
                 'I want…to change things. I want to believe that anything can be changed. The moment I met you, a new world opened up for me. You see, after wandering in the darkness for so long, a light brought me happiness. It’s all thanks to you. – Chrono',
                 'Moving on doesn’t mean you forget about things. It just means you have to accept what’s happened and continue living. – Erza Scarlet',
                 'Do you always want to live hiding behind the mask you put up for the sake of others? You’re you, and there’s nothing wrong with that. – Ymir',
                 'The ticket to the future is always open. – Vash The Stampede',
                 'People become stronger because they have memories they can’t forget. – Tsunade',
                 'If you only face forward, there is something you will miss seeing. – Vash the Stampede',
                 'Don’t live your life making up excuses. The one making your choices is yourself! – Mugen',
                 'I hate perfection. To be perfect is to be unable to improve any further. – Kurotsuchi Mayuri',
                 'If your life can change once, your life can change again. – Sanae Furukawa',
                 'Hurt me with the truth. But never comfort me with a lie. – Erza Scarlet',
                 'A place where someone still thinks about you is a place you can call home. – Jiraiya',
                 'Vision is not what your eyes see, but an image that your brain comprehends. – Touko Aozaki',
                 'Knowing what it feels to be in pain, is exactly why we try to be kind to others. – Jiraiya',
                 'How can you move forward if you keep regretting the past? – Edward Elric',
                 'If you just submit yourself to fate, then that’s the end of it. – Keiichi Maebara',
                 'Being alone is better than being with the wrong person. – L Lawliet',
                 'Sometimes I do feel like I’m a failure. Like there’s no hope for me. But even so, I’m not gonna give up. Ever! – Izuku Midoriya',
                 'Tears are how our heart speaks when your lips cannot describe how much we’ve been hurt. – Jellal Fernandes',
                 'There are no regrets. If one can be proud of one’s life, one should not wish for another chance. – Saber',
                 'You can’t always hold on to the things that are important. By letting them go we gain something else. – Kunio Yaobi',
                 'The circumstances of one’s birth are irrelevant, but it is what you do with the gift of life that determines who you are. – Pokemon',
                 'Do not think about other things, there is only one thing you can do. So master that one thing. Do not forget. What you must imagine is always that you, yourself, are the strongest. You do not need outside enemies. For you, the one you have to fight is none other than your own image. – Archer',
                 'The best way to remove your lies is to make them come true. – Suzaku Kururugi',
                 'You can’t sit around envying other people’s worlds. You have to go out and change your own. – Shinichi Chiaki',
                 'What is right? What is wrong? In this mixed up world, deciding what is right and wrong is not easy. You can’t just go by somebody else’s rules. If you let yourself be controlled like that, you’ll just become a puppet that can’t make decisions on its own. You have to live by your rules. – Gintoki Sakata',
                 'Life is like a tube of toothpaste. When you’ve used all the toothpaste down to the last squeeze, that’s when you’ve really lived. Live with all your might, and struggle as long as you have a life. – Mion Sonozaki',
                 'Fools who don’t respect the past are likely to repeat it. – Nico Robin',
                 'That’s why I can’t make a change. Everything I do is so… Half-assed. – Hiroshi Kido',
                 'Sometimes it’s necessary to do unnecessary things. – Kanade Jinguuji',
                 'An excellent leader must be passionate because it’s their duty to keep everyone moving forward. – Nico Yazawa',
                 'Just like games, no matter how well you have things lined up in your life, there’s always something to keep you on your toes. – Junichirou Kagami',
                 'Do exactly as you like. That is the true meaning of pleasure. Pleasure leads to joy and joy leads to happiness.  – Gilgamesh',
                 'If you can’t do something, then don’t. Focus on what you can do. – Shiroe',
                 'When you lose sight of your path, listen for the destination in your heart. – Allen Walker',
                 'A skyscraper built within your mind will never fall down. – Kill la Kill',
                 'The only home that a man should ever need is within his heart. – Lavi Bookman',
                 'A dream is worth less than nothing if you don’t have someone else to share it. – Dousan Saitou',
                 'You’ll only realize that you truly love someone if they already caused you enormous pain. Your enemies can never hurt you the way your loved ones can. It’s the people close to your heart that can give you the most piercing wound. Love is a double-edged sword, it can heal the wound faster or it can sink the blade even deeper. – Kenshin Himura',
                 'I do not need a Heaven. However, if I must go to Heaven then please, God, do not divide Heaven in two. Please do not divide the robots from the humans. – Chiisana Hoshi yo Yume',
                 'Simplicity is the easiest path to true beauty. – Seishuu Handa',
                 'What you can’t accomplish alone, becomes doable when you’re with someone else. – Taichi Yaegashi',
                 'If you turn your eyes away from sad things, they’ll happen again one day. If you keep running away, you’ll keep repeating the same mistakes. That’s why you have to face the truth straight on. – Riki Naoe',
                 'Even if we forget the faces of our friends, We will never forget the bonds that were carved into our souls. – Otonashi Yuzuru',
                 'To act is not necessarily compassion. True compassion sometimes comes from inaction. – Hinata Miyake',
                 'It’s impossible to work hard for something you don’t enjoy. – Silica',
                 'Life is not a game of luck. If you wanna win, work hard. – Sora']
        emb = discord.Embed(
            title = 'Anime Quote For Ya',
            description = f'{ctx.message.author.mention} "{random.choice(quote)}"',
            color = ctx.author.color)
        emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.reply(embed = emb)

def setup(bot):
    bot.add_cog(Quotes(bot))