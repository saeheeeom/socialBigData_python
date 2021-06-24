# 어떤 문서의 topic을 분석하려고 할 때 사용
# model 만드는 과정: 어떤 topic을 다루는 텍스트를 만들 때 어떤 단어 사용해야 할까?
# 반대로 model 쓸 때는 이 글에서 다루는 topic은 무엇인가? 도출해낼 수 있음
# model을 쓴 결과: 각 문서의 토픽 분포, 각 토픽의 단어 분포
# 각 문서의 토픽분포: 문서별로 토픽별 proportion 제시
# 토픽별 단어분포: 모든 단어 리스트를 가져와서, 토픽별로 어떤 단어를 쓸 확률 제시

from gensim.models import ldamodel, coherencemodel
from gensim import corpora # 데이터 전처리.

# 이 밑부분은 토큰화된 문자열 리스트의 리스트 tc 가져오려고
# testWord2Vec에서 복붙한 내용 (명사만 가져오는 부분은 추가함)

from gensim.models import Word2Vec
from webcrawling import getTitleClien
from netminerClientPy import _NLP # 형태소 분석

titleList = getTitleClien(5)
tc = []
for title in titleList:
    mr_result = _NLP.MorphKR.getMorpheme(title)
    tmpList = []
    for i in mr_result:
        word = i[0]
        tag = i[1]
        if 'NN' in tag: # 문자열 중 명사만
            tmpList.append(word) # 크롤링한 문자열들을 _NLP로 형태소 수준으로 쪼갬 -> tmpList에 넣기
    tc.append(tmpList)

#dic = corpora.Dictionary(토큰화된 문자열 리스트의 리스트)
dic = corpora.Dictionary(tc)
corpus = []
for title in tc: # getTitleClien이었으니까 제목
    corpus.append(dic.doc2bow(title))

ldaModel1 = ldamodel.LdaModel(corpus, num_topics=5, id2word = dic, passes = 5)

topics = ldaModel1.print_topics(num_words=3)
for tp in topics:
    print(tp[0], tp[1])

# model 토픽 평가
coherence_model_lda = coherencemodel.CoherenceModel(model=ldaModel1, corpus=corpus, coherence='u_mass')

coherence_lda = coherence_model_lda.get_coherence()
print(coherence_lda) # 일관성: 작을수록 주제별 겹치는 단어 적다
print(ldaModel1.log_perplexity(corpus)) # 혼란도: 작을수록 모델이 실제문헌 정보 잘 반영했다