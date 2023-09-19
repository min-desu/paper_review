import math, jieba

# 文本分词函数，这里使用了jieba
def tokenize(text):
    return list(jieba.cut(text))

# 词频统计
def calculate_tf(text):
    tf_dict = {}
    tokens = tokenize(text)
    for token in tokens:
        tf_dict[token] = tf_dict.get(token, 0) + 1
    return tf_dict

# 利用TF向量计算余弦相似度
def cosine_similarity(tf1, tf2):
    dot_product = sum(tf1.get(term, 0) * tf2.get(term, 0) for term in set(tf1) & set(tf2))
    magnitude1 = math.sqrt(sum(tf1[term] ** 2 for term in tf1))
    magnitude2 = math.sqrt(sum(tf2[term] ** 2 for term in tf2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # 避免除以零
    return dot_product / (magnitude1 * magnitude2)

if __name__ == "__main__":
    doc = [
        "第一篇文档的内容",
        "第二	篇文档的内容"
    ]

    tf1 = calculate_tf(doc[0])
    tf2 = calculate_tf(doc[1])

    similarity = cosine_similarity(tf1, tf2)
    print(f"文档1与文档2的余弦相似度：{similarity}")
