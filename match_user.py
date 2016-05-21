


def die(arg):
	print('Runtime error:',arg)
	raise Exception


def calcAttrSimilarity(attr1, attr2, weight):
	if len(attr1) != len(attr2): die('len attr1 and len attr2 mismatch.')
	if len(attr1) != len(weight): die('len attr and len weight mismatch.')
	nsame = 0	
	for i in range(len(attr1)):
		char1 = attr1[i]
		char2 = attr2[i]
		nsame += (char1 == char2) * weight[i]
	return int(nsame)

def getUnSeenUsers(like, dislike):
	lenMatrix = 100
	matrix = [1]*lenMatrix
	for string in (like, dislike):
		if len(string)%2 != 0: die('len of like and dislike should be even but got odd')
		for i in range(int(len(string)/2)):
			uid = int(string[2*i:2*i+2])
			matrix[uid] = 0
	UnseenUsers = []
	for i in range(lenMatrix):
		if matrix[i]: UnseenUsers.append(i)
	return UnseenUsers

def getUserAttr(db,uid):
	user = db.user.query.filter_by(id=uid)
	if user == null: die('expect user got null.')
	return user.exiting

def getUserLikeDislike(db,uid):
	user = db.user.query.filter_by(id=uid)
	if user == null: die('expect user got null.')
	return (user.like,user.dislike)

def getMatchedUser(db,uid):
	attrUser = getUserAttr(db,uid)
	likeDislike = getUserLikeDislike(db,uid)
	UnseenUsers = getUnSeenUsers(likeDislike[0],likeDislike[1])



def test1():
	a = 0b1111101111
	b = 0b1111111111
	weight = (10,10,10,10,10,10,10,10,10,10)
	print(calcAttrSimilarity(a,b,10,weight))

def test2():
	a = [('xiaoming',20),('zhangsan',40),('nidie',10)]
	print(sorted(a,key=lambda x : x[1]))

def test3():
	like = '000204060899'
	dislike = '010798'
	print(getUnSeenUsers(like,dislike))
test3()