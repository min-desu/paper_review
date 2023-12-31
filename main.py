import math, jieba, sys

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
    if len(sys.argv)!=4:
        print("please input files name\n")
        exit(0)
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            doc0 = f.read()
        f.close()
    except Exception as e:
        print("无法读取第一篇文件\n")
        exit()
    try:
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            doc1 = f.read()
        f.close()
    except Exception as e:
        print("无法读取第二篇文件\n")
        exit()
    tf1 = calculate_tf(doc0)
    tf2 = calculate_tf(doc1)

    similarity = cosine_similarity(tf1, tf2)
    result = "%.2f" % similarity
    try:
        f = open(sys.argv[3], 'w+', encoding='utf-8')
        f.write(f"文档1与文档2的相似度：{result}")
        f.close()
    except Exception as e:
        print("无法写入结果文件\n")
        exit()
