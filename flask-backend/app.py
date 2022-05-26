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