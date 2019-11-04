import random

#创建35份试卷，问下列省份的省会是哪里，每份试卷的问题的顺序都不一样，防止抄袭。

#包含省份和省会的字典
capitals = {'湖南':'长沙',
            '湖北':'武汉',
            '广东':'广州',
            '广西':'南宁',
            '河北':'石家庄',
            '河南':'郑州',
            '山东':'济南',
            '山西':'太原',
            '江苏':'南京',
            '浙江':'杭州',
            '江西':'南昌',
            '黑龙江':'哈尔滨',
            '新疆':'乌鲁木齐',
            '内蒙古':'呼和浩特',
            '云南':'昆明',
            '贵州':'贵阳',
            '福建':'福州',
            '吉林':'长春',
            '安徽':'合肥',
            '四川':'成都',
            '西藏':'拉萨',
            '宁夏':'银川',
            '辽宁':'长春',
            '青海':'西宁',
            '甘肃':'兰州',
            '陕西':'西安',
            '台湾':'台北',
            '北京':'北京',
            '上海':'上海',
            '天津':'天津',
            '重庆':'重庆',
            '香港':'香港',
            '澳门':'澳门'}

#创建35份试卷,每次循环就会生成一份试卷。
for quizNum in range(35):

    # 创建问卷文件和答案文件
    quizFile = open('试卷%s.txt' % (quizNum + 1), 'w', encoding='utf-8')
    answerFile = open('答案%s.txt' % (quizNum + 1), 'w')

    #写入试卷的头部
    quizFile.write('姓名:\t\t\t\t日期:\n\n')
    quizFile.write('\n\n')

    #随机打乱省份的顺序,使每份试卷的问题顺序都不一样
    allProvinces = list(capitals.keys())
    random.shuffle(allProvinces)

    #开始循环设置答案选项，多少个省份就有多少道问题。
    for questionNum in range(len(capitals)):
        #获取正确答案和其他三个错误答案

        #这里的正确答案就是此次循环到的省份对应的省会。
        correctAnswer = capitals[allProvinces[questionNum]]

        #这里的错误答案就是随机获取除此次循环对应省份的省会之外的3个省会即可。
        allCapitalList = list(capitals.values())

        #删除本次循环省份的省会
        del allCapitalList[allCapitalList.index(correctAnswer)]

        #在已经删除掉正确省会的列表中随机选取三个省会
        wrongAnswers = random.sample(allCapitalList, 3)

        #将错误答案和正确答案的列表相加获得本次循环（本题）的4个回答选项的一个列表。
        answerOptions = wrongAnswers + [correctAnswer]

        #随机打乱生成的回答选项的顺序,否则正确答案都是第四个选项（D）
        random.shuffle(answerOptions)

        #写入问题到试卷文件
        quizFile.write('{}. {}的省会是哪里？\n'.format(questionNum + 1, allProvinces[questionNum]))

        #开始写入每题的四个选项,每题循环4次
        for i in range(4):
            quizFile.write(' {}. {}\n'.format('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        # 将正确回答写入答案文件
        answerFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    #设置为每个试卷的问题和答案就可以关闭这个试卷文件和答案文件
    quizFile.close()
    answerFile.close()
