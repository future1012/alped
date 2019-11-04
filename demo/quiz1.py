import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'湖南':'长沙','湖北':'武汉','广东':'广州','广西':'南宁','河北':'石家庄','河南':'郑州','山东':'济南','山西':'太原','江苏':'南京','浙江':'杭州','江西':'南昌','黑龙江':'哈尔滨','新疆':'乌鲁木齐','云南':'昆明','贵州':'贵阳','福建':'福州','吉林':'吉林','安徽':'合肥','四川':'成都','西藏':'拉萨','宁夏':'银川','辽宁':'长春','青海':'西宁','甘肃':'兰州','陕西':'太原','内蒙古':'呼和浩特','台湾':'台北','北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','香港':'香港','澳门':'澳门'}

# Generate 35 quiz files.

for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('试卷%s.txt' % (quizNum + 1), 'w', encoding='utf-8')
    answerKeyFile = open('答案%s.txt' % (quizNum + 1), 'w')
    # Write out the header for the quiz.
    quizFile.write('姓名:\t\t\t\t日期:\n\n')
    quizFile.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(len(capitals)):
        #Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. %s的省会是哪里？\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
        answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
