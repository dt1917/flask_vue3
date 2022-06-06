from flask import Flask,jsonify 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET","POST"])
def get_echo_call():
    return jsonify({
    "newsObjs":[
        {
        "id": 0,
        "pressName" : "YTN",
        "newsTop" : [
            {
                "rank":0,
                "title" : "외제차 부부 주차를 항상 이따위로짜증납니다",
                "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                "summary" : "요약1",
                "fullContent": "데일리안 = 이지희 기자 주차 공간이 남아 있어도 꿋꿋이 통로에 차량을 세우는 한 부부의 행태가 온라인상에서 공분을 사고 있다ⓒ보배드림5일 온라인 커뮤니티 보배드림에는 항상 이기적인 주차하는 부부 X짜증나네요라는 제목의 글이 올라왔다작성자는 항상 주차 자리가 비어있어도 저따위로 주차하는 흰색 E클래스가 있다며 같은 라인 사는 아줌마인데 오늘 보니 그 남편차가 Q7이더라 아주 둘이 꿍짝이 잘 맞는지 어쩜 주차라인 안에 차를 집어넣은 걸 본적이 없다고 불만을 드러냈다이어 원래 통로자리에는 밤에 자리가 없으면 한 줄로 세우긴 하는데 아파트 규칙에 따르면 아침에는 차를 빼야한다며 저 차량은 매번 저런다고 지적했다작성자가 공개한 사진에 따르면 아우디Q7 차량이 한쪽 벽면에도 제대로 밀착돼있지 않은 채 통로에 주차돼 있다작성자는 댁들 차만 소중한가라며 자리 없을 때만 통로주차 허용한 거지 아무 때나 대라고 허락한 게 아니다라고 분노했다그러면서 E클래스 아줌마도 Q7 아저씨도 그 차 두 대가 본인들 전 재산인지 아주 끔찍이 아끼는 건지 아니면 주차칸에 주차할 실력이 부족한 건지 제발 남들에게 피해 주지 말고 자리 비어있으면 주차 공간 안에 주차합시다라고 강조했다해당 사연에 누리꾼들은 배려해주면 이기적으로 악용하는 사람들이 꼭 있더라 사진 찍어서 아파트 엘리베이터에 부착하세요 평소 습관 같다 어느 아파트나 주차빌런은 있구나 공용공간에서 이기적으로 살지 맙시다라는 반응을 보였다"},
            
            {   
                "rank":1,
                "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                "voice_url" : "",
                "summary" : "요약2",
                "fullContent": "내용2"},
            
            {
                "rank":2,
                "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                "voice_url" : "",
                "summary" : "요약3",
                "fullContent": "내용3"},
            
            {
                "rank":3,
                "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                "voice_url" : "",
                "summary" : "요약4",
                "fullContent": "내용4"},
            
            {
                "rank":4,
                "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                "voice_url" : "",
                "summary" : "요약5",
                "fullContent": "내용5"}
            ]
        
        },

        {
            "id": 1,
            "pressName" : "한겨례",
            "newsTop" : [
                {
                    "rank":0,
                    "title" : "[속보] [단독] 내일 국무회의에 집무실 이전 예비비 안건 상정",
                    "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                    "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                    "summary" : "요약1",
                    "fullContent": "내용1"},
                
                {   
                    "rank":1,
                    "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                    "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약2",
                    "fullContent": "내용2"},
                
                {
                    "rank":2,
                    "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                    "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약3",
                    "fullContent": "내용3"},
                
                {
                    "rank":3,
                    "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                    "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약4",
                    "fullContent": "내용4"},
                
                {
                    "rank":4,
                    "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                    "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약5",
                    "fullContent": "내용5"}
                ]
        },
        {
            "id": 2,
            "pressName" : "동아일보",
            "newsTop" : [
                {
                    "rank":0,
                    "title" : "[속보] [단독] 내일 국무회의에 집무실 이전 예비비 안건 상정",
                    "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                    "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                    "summary" : "요약1",
                    "fullContent": "내용1"},
                
                {   
                    "rank":1,
                    "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                    "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약2",
                    "fullContent": "내용2"},
                
                {
                    "rank":2,
                    "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                    "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약3",
                    "fullContent": "내용3"},
                
                {
                    "rank":3,
                    "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                    "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약4",
                    "fullContent": "내용4"},
                
                {
                    "rank":4,
                    "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                    "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약5",
                    "fullContent": "내용5"}
                ]
        },
        {
            "id": 3,
            "pressName" : "조선일보",
            "newsTop" : [
                {
                    "rank":0,
                    "title" : "[속보] [단독] 내일 국무회의에 집무실 이전 예비비 안건 상정",
                    "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                    "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                    "summary" : "요약1",
                    "fullContent": "내용1"},
                
                {   
                    "rank":1,
                    "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                    "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약2",
                    "fullContent": "내용2"},
                
                {
                    "rank":2,
                    "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                    "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약3",
                    "fullContent": "내용3"},
                
                {
                    "rank":3,
                    "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                    "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약4",
                    "fullContent": "내용4"},
                
                {
                    "rank":4,
                    "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                    "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약5",
                    "fullContent": "내용5"}
                ]
        },
        {
            "id": 4,
            "pressName" : "JTBC",
            "newsTop" : [
                {
                    "rank":0,
                    "title" : "[속보] [단독] 내일 국무회의에 집무실 이전 예비비 안건 상정",
                    "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                    "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                    "summary" : "요약1",
                    "fullContent": "내용1"},
                
                {   
                    "rank":1,
                    "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                    "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약2",
                    "fullContent": "내용2"},
                
                {
                    "rank":2,
                    "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                    "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약3",
                    "fullContent": "내용3"},
                
                {
                    "rank":3,
                    "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                    "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약4",
                    "fullContent": "내용4"},
                
                {
                    "rank":4,
                    "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                    "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약5",
                    "fullContent": "내용5"}
                ]
        },
        {
            "id": 5,
            "pressName" : "뉴스1",
            "newsTop" : [
                {
                    "rank":0,
                    "title" : "[속보] [단독] 내일 국무회의에 집무실 이전 예비비 안건 상정",
                    "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                    "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                    "summary" : "요약1",
                    "fullContent": "내용1"},
                
                {   
                    "rank":1,
                    "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                    "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약2",
                    "fullContent": "내용2"},
                
                {
                    "rank":2,
                    "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                    "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약3",
                    "fullContent": "내용3"},
                
                {
                    "rank":3,
                    "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                    "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약4",
                    "fullContent": "내용4"},
                
                {
                    "rank":4,
                    "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                    "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약5",
                    "fullContent": "내용5"}
                ]
        },
        {
            "id": 6,
            "pressName" : "서울경제",
            "newsTop" : [
                {
                    "rank":0,
                    "title" : "[속보] [단독] 내일 국무회의에 집무실 이전 예비비 안건 상정",
                    "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                    "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                    "summary" : "요약1",
                    "fullContent": "내용1"},
                
                {   
                    "rank":1,
                    "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                    "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약2",
                    "fullContent": "내용2"},
                
                {
                    "rank":2,
                    "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                    "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약3",
                    "fullContent": "내용3"},
                
                {
                    "rank":3,
                    "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                    "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약4",
                    "fullContent": "내용4"},
                
                {
                    "rank":4,
                    "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                    "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약5",
                    "fullContent": "내용5"}
                ]
        },
        {
            "id": 7,
            "pressName" : "연합뉴스TV",
            "newsTop" : [
                {
                    "rank":0,
                    "title" : "[속보] [단독] 내일 국무회의에 집무실 이전 예비비 안건 상정",
                    "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                    "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                    "summary" : "요약1",
                    "fullContent": "내용1"},
                
                {   
                    "rank":1,
                    "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                    "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약2",
                    "fullContent": "내용2"},
                
                {
                    "rank":2,
                    "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                    "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약3",
                    "fullContent": "내용3"},
                
                {
                    "rank":3,
                    "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                    "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약4",
                    "fullContent": "내용4"},
                
                {
                    "rank":4,
                    "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                    "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약5",
                    "fullContent": "내용5"}
                ]
        },
        {
            "id": 8,
            "pressName" : "KOREA",
            "newsTop" : [
                {
                    "rank":0,
                    "title" : "[속보] [단독] 내일 국무회의에 집무실 이전 예비비 안건 상정",
                    "url" : "https://n.news.naver.com/article/052/0001721717?ntype=RANKING",
                    "voice_url" : "http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3",
                    "summary" : "요약1",
                    "fullContent": "내용1"},
                
                {   
                    "rank":1,
                    "title" : "'가평 계곡 살인' 공개수배 엿새째...'깊이 4m 계곡에서 범행'",
                    "url" : "https://n.news.naver.com/article/052/0001721692?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약2",
                    "fullContent": "내용2"},
                
                {
                    "rank":2,
                    "title" : "[속보] BTS 올해도 그래미상 고배...도자캣&시저 수상",
                    "url" : "https://n.news.naver.com/article/052/0001721713?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약3",
                    "fullContent": "내용3"},
                
                {
                    "rank":3,
                    "title" : "이재명, 팬카페 등판 '개딸·개삼촌 사랑 감사' ",
                    "url" : "https://n.news.naver.com/article/052/0001721688?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약4",
                    "fullContent": "내용4"},
                
                {
                    "rank":4,
                    "title" : "신규 확진 일주일 만에 10만 명대...완화된 거리두기 시작",
                    "url" : "https://n.news.naver.com/article/052/0001721634?ntype=RANKING",
                    "voice_url" : "",
                    "summary" : "요약5",
                    "fullContent": "내용5"}
                ]
        }
    ]
})


app.run(host='127.0.0.1', port=5000)