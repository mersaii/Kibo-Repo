import os
import re
import heapq

class FileAnalyzer:
    def __init__(self):
        # The inverted index, which maps words (strings) to heaps.
        # Each heap is represented as a list of tuples, where each
        # tuple represents information about the occurrences of that
        # word in a document.
        #
        # For example:
        # 'hello' -> [ (5, 'example1.txt', [ <lines where 'hello' appears)],
        #              (3, 'example2.txt', [ <lines where 'hello' appears)],
        #              ... ]
        self.index = {}

    def sift_down_helper_function(self, array, begin, limit):
        parent = begin
        while parent * 2 + 1 < limit:
            largest_child = parent * 2 + 1
            if largest_child + 1 < limit and array[largest_child] < array[largest_child + 1]:
                largest_child += 1
            if array[parent] < array[largest_child]:
                array[parent], array[largest_child] = array[largest_child], array[parent]
                parent = largest_child
            else:
                return
    # Task 1
    def heapify_example(self):
        given_list = [2, 10, 25, 5, 12, 16, 28]
        iteration_steps = [given_list[:]]
        for i in range(len(given_list) // 1, -1, -1):
            self.sift_down_helper_function(given_list, i, len(given_list))
            iteration_steps.append(given_list[:])

        return iteration_steps

    # Task 2
    def add_document(self, filename):
        word_frequency = {}
        line_digit_tracker = 0

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line_digit_tracker += 1
                # Convert to lowercase and remove commas, periods, and newlines
                cleaned_line = re.sub(r'[,.\n]', '', line.lower())
                words = cleaned_line.split()
                for word in words:
                    if word not in word_frequency:
                        word_frequency[word] = {'word_frequency': 0, 'word_contexts': []}
                    word_frequency[word]['word_frequency'] += 1
                    word_frequency[word]['word_contexts'].append(line)

        for key, value in word_frequency.items():
            if key not in self.index:
                self.index[key] = []
            heapq.heappush(self.index[key], (-value['word_frequency'], filename, value['word_contexts']))

    # Task 3
    def top_k_documents(self, word, k):
        # error checking
        if word not in self.index:
            return []

        word_heap = self.index[word][:]
        top_documents = []
        for i in range(min(k, len(word_heap))):
            top_documents.append(heapq.heappop(word_heap)[1])

        return top_documents

    # Task 4
    def top_k_contexts(self, word, k):
        # error checking
        if word not in self.index:
            return []

        word_heap = self.index[word][:]
        word_contexts = []
        for _ in range(min(k, len(word_heap))):
            word_freq, word_documents, contexts = heapq.heappop(word_heap)
            for context in contexts:
                if len(word_contexts) < k:
                    word_contexts.append(context)
                else:
                    break

        return word_contexts

    # Task 5
    def similarity_score(self, str1, str2):
        memory=None

        # Base cases: If one of the strings is empty,
        # return the length of the other string
        if memory is None:
            memory = {}

        if (str1, str2) in memory:
            return memory[(str1, str2)] 
        if len(str1) == 0:
            return len(str2)
        if len(str2) == 0:
            return len(str1)

        # If the first characters of the strings are the same,
        # no operation is needed
        if str1[0] == str2[0]:
            memory[(str1, str2)] = self.similarity_score(str1[1:], str2[1:])

        # Otherwise, find the minimum of three operations:
        # insert, delete, or replace
        else:
            insert_cost = self.similarity_score(str1, str2[1:])
            delete_cost = self.similarity_score(str1[1:], str2)
            replace_cost = self.similarity_score(str1[1:], str2[1:])
            memory[(str1, str2)] = min(insert_cost, delete_cost, replace_cost) + 1

        return memory[(str1, str2)]

    # Note: you should not modify this function.
    def document_similarity(self, file1, file2):
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()[:250]
            content2 = f2.read()[:250]
        return self.similarity_score(content1, content2)

    # Note: you should not modify this function.
    def document_similarities(self, folder_path):
        print('\nNote: the similarity score calculation will not work efficiently until Task 5 is completed.')
        files = os.listdir(folder_path)
        for i in range(len(files)):
            for j in range(i + 1, len(files)):
                print('  Similarity score between ' + files[i] + ' and ' + files[j] + ': ', end='', flush=True)
                print(self.document_similarity(os.path.join(folder_path, files[i]), os.path.join(folder_path, files[j])))

# Example usage.
if __name__ == "__main__":
    analyzer = FileAnalyzer()
    analyzer.add_document('examples/example1.txt')
    analyzer.add_document('examples/example2.txt')
    analyzer.add_document('examples/example3.txt')
    analyzer.add_document('examples/example4.txt')
    print(analyzer.top_k_documents('earthquake', 3))
    print(analyzer.top_k_contexts('earthquake', 5))
    analyzer.document_similarities('examples')

