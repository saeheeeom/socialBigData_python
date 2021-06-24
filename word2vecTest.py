# 단어의 특성을 벡터로 나타내는 것이 word2vec
# 단어의 의미 사이 거리를 벡터 공간에서 계산할 수 있음
# 벡터 공간에서의 연산도 가능 (kink->kings, queen->queens 만드는 연산 동일)

from gensim.models import Word2Vec

# 학습 모델 생성
model1 = Word2Vec(vector_size=50, window=2, min_count=5, workers=4, sg=0)
# size = 총 벡터 크기
# window : 인접 단어 몇 단계 (앞, 뒤로 각각 몇 개) 까지 연관 단어로 보느냐
# min_count : 빈도수 5번 이상인 단어만 분석 대상이다
# workers : 쿼드코어 cpu 사용
# sg : CBOW 알고리즘 사용

# 모델에 단어 구축
model1.build_vocab(tc)
# 여기 안에 들어갈 인자는, 리스트로 이루어진 리스트, 그리고 그 리스트는 쪼개진 문자열로 이루어짐

# 모델 학습
model1.train(tc, total_examples=len(tc), epochs=5)
# epoch: 학습 횟수

# 실제 실습은 testWord2Vec 에서 계속