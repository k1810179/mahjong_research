#=======================================================================================
#通常手のシャンテン数を算出するpythonスクリプト
#=======================================================================================

paiType = [
	{"No":0,"paiName":"赤五萬","cssSprite":"man0","paigaNo":4},
	{"No":1,"paiName":"一萬","cssSprite":"man1","paigaNo":0},
	{"No":2,"paiName":"二萬","cssSprite":"man2","paigaNo":1},
	{"No":3,"paiName":"三萬","cssSprite":"man3","paigaNo":2},
	{"No":4,"paiName":"四萬","cssSprite":"man4","paigaNo":3},
	{"No":5,"paiName":"五萬","cssSprite":"man5","paigaNo":5},
	{"No":6,"paiName":"六萬","cssSprite":"man6","paigaNo":6},
	{"No":7,"paiName":"七萬","cssSprite":"man7","paigaNo":7},
	{"No":8,"paiName":"八萬","cssSprite":"man8","paigaNo":8},
	{"No":9,"paiName":"九萬","cssSprite":"man9","paigaNo":9},

	{"No":10,"paiName":"赤五筒","cssSprite":"pin0","paigaNo":14},
	{"No":11,"paiName":"一筒","cssSprite":"pin1","paigaNo":10},
	{"No":12,"paiName":"二筒","cssSprite":"pin2","paigaNo":11},
	{"No":13,"paiName":"三筒","cssSprite":"pin3","paigaNo":12},
	{"No":14,"paiName":"四筒","cssSprite":"pin4","paigaNo":13},
	{"No":15,"paiName":"五筒","cssSprite":"pin5","paigaNo":15},
	{"No":16,"paiName":"六筒","cssSprite":"pin6","paigaNo":16},
	{"No":17,"paiName":"七筒","cssSprite":"pin7","paigaNo":17},
	{"No":18,"paiName":"八筒","cssSprite":"pin8","paigaNo":18},
	{"No":19,"paiName":"九筒","cssSprite":"pin9","paigaNo":19},

	{"No":20,"paiName":"赤五索","cssSprite":"sou0","paigaNo":24},
	{"No":21,"paiName":"一索","cssSprite":"sou1","paigaNo":20},
	{"No":22,"paiName":"二索","cssSprite":"sou2","paigaNo":21},
	{"No":23,"paiName":"三索","cssSprite":"sou3","paigaNo":22},
	{"No":24,"paiName":"四索","cssSprite":"sou4","paigaNo":23},
	{"No":25,"paiName":"五索","cssSprite":"sou5","paigaNo":25},
	{"No":26,"paiName":"六索","cssSprite":"sou6","paigaNo":26},
	{"No":27,"paiName":"七索","cssSprite":"sou7","paigaNo":27},
	{"No":28,"paiName":"八索","cssSprite":"sou8","paigaNo":28},
	{"No":29,"paiName":"九索","cssSprite":"sou9","paigaNo":29},

	{"No":30,"paiName":"裏","cssSprite":"ji0","paigaNo":30},
	{"No":31,"paiName":"東","cssSprite":"ji1","paigaNo":31},
	{"No":32,"paiName":"南","cssSprite":"ji2","paigaNo":32},
	{"No":33,"paiName":"西","cssSprite":"ji3","paigaNo":33},
	{"No":34,"paiName":"北","cssSprite":"ji4","paigaNo":34},
	{"No":35,"paiName":"白","cssSprite":"ji5","paigaNo":35},
	{"No":36,"paiName":"發","cssSprite":"ji6","paigaNo":36},
	{"No":37,"paiName":"中","cssSprite":"ji7","paigaNo":37}
]

#============================================================================
#グローバル変数
#============================================================================
#tehai = new Array(37); # 手牌の配列：37種
tehai = [0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0] # 手牌の配列：37種
#preTempTehai = new Array(37) # tempTehaiの前処理用クローン。事前に完全メンツや孤立牌を抜いておく
#tempTehai = new Array(37) # tehai配列のクローン
preTempTehai=[]; # tempTehaiの前処理用クローン。事前に完全メンツや孤立牌を抜いておく
tempTehai=[]; # tehai配列のクローン
red5manCount = 0; # 赤5マンの数
red5pinCount = 0; # 赤5ピンの数
red5souCount = 0; # 赤5ソウの数

#マンズ関連
manMentsuMax = 0
manTaatsuMax = 0

#ピンズ関連
pinMentsuMax = 0
pinTaatsuMax = 0

#ソーズ関連
souMentsuMax = 0
souTaatsuMax = 0

#字牌関連
jiTaatsuMax = 0

preMentsuCount = 0 # kanzen_koutsu_suuとkanzen_shuntsu_suu格納用
koutsuCount = 0 # コーツ数カウント用
#============================================================================
#赤ドラの有無をチェックしてカウントする処理【赤ドラのカウントを事前にしなかった場合に使う】
#各赤ドラはtehai配列の0，10，20番地にあるものとする
#============================================================================
def checkReddora():
    # グローバル変数の初期化
    red5manCount = 0 # 赤5マンの数
    red5pinCount = 0 # 赤5ピンの数
    red5souCount = 0 # 赤5ソウの数

    # 赤五萬の有無をチェックしてカウントする
    if(tehai[0]):
        red5manCount += tehai[0] # 赤五萬の牌数を追加
    # 赤五筒の有無をチェックしてカウントする
    if(tehai[10]):
        red5pinCount += tehai[10] # 赤五筒の牌数を追加
    # 赤五索の有無をチェックしてカウントする
    if(tehai[20]):
        red5souCount += tehai[20] # 赤五索の牌数を追加

def main():
    checkReddora()
    print(tehai)
    print(red5manCount)

if __name__ == "__main__":
    main()