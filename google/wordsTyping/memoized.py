class Solution:
  def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
    if any([len(word) > cols for word in sentence]):
      return 0

    result = 0
    rows_left = rows
    memo = {}
    sentence_length = sum(map(len, sentence)) + len(sentence)
    word_idx = 0
    while rows_left:
      if word_idx in memo:
        count, word_idx = memo[word_idx]
        result += count
      else:
        start_word_idx = word_idx
        count = 0
        cols_left = cols
        while cols_left:
          word_len = len(sentence[word_idx])
          # Cases when cols is 10000 and sentence is ['a']
          if cols_left // sentence_length > 0:
            fits_times, reminder = divmod(cols_left, sentence_length)
            count += fits_times
            cols_left = reminder

          if word_len > cols_left:
            break

          cols_left -= (word_len + 1)
          if word_idx == len(sentence) - 1:
            count += 1  
          word_idx = (word_idx + 1) % len(sentence)

        memo[start_word_idx] = (count, word_idx)
        result += count
      rows_left -= 1
    return result