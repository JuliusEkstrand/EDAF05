import sys
from graph import Graph

#processes in terms of lines, not used anymore
def process_input(input_data):
    lines = []
    for line in input_data.splitlines():
        lines.append(line)
    return lines

def add_words_to_graph(words, graph):
    for i in range(len(words)):
        graph.add_vertex(words[i])
        for j in range(len(words)):
            if i != j:
                if compare_words(words[i],words[j]):
                    graph.add_vertex_and_edge(words[i],words[j])

def compare_words(word1, word2):
    last_four = word1[-4:]
    for letter in last_four:
        if letter not in word2:
            return False
        elif word2.count(letter) < last_four.count(letter):
            return False
    return True

def perform_queries(graph, line):
    parts = line.split()
    word1 = parts[0]
    word2 = parts[1]
    print(graph.BFS(word1, word2))

def main(output_file = None):

    input_data = sys.stdin.read().strip()
    input_list = process_input(input_data)

    parts = input_list[0].split()
    num_words = int(parts[0])
    num_queries = int(parts[1])

    words = input_list[1:num_words + 1]
    queries = input_list[num_words + 1:]

    graph = Graph()

    add_words_to_graph(words, graph)

    for query in queries:
        perform_queries(graph, query)


if __name__ == "__main__":
    main()