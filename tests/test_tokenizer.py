

def test_tokenize(tokenizer):
    sample_text = ('Секретарша (Петрова-Водкина) ставила '
                   'сургучные- печати на пакет, '
                   'посетители ожидали своей очереди, '
                   'радио играло сентиментальный вальс... '
                   'А Вася писал в вк: "Как дела?))"')

    tokens, spaces = tokenizer(sample_text)

    assert tokens == ['Секретарша',
                      '(',
                      'Петрова-Водкина',
                      ')',
                      'ставила',
                      'сургучные',
                      '-',
                      'печати',
                      'на',
                      'пакет',
                      ',',
                      'посетители',
                      'ожидали',
                      'своей',
                      'очереди',
                      ',',
                      'радио',
                      'играло',
                      'сентиментальный',
                      'вальс',
                      '.',
                      '.',
                      '.',
                      'А',
                      'Вася',
                      'писал',
                      'в',
                      'вк',
                      ':',
                      '"',
                      'Как',
                      'дела',
                      '?',
                      ')',
                      ')',
                      '"']

    # Test text restoring
    assert ''.join([f'{t}{" " * int(s)}'
                   for t, s in zip(tokens, spaces)]) == sample_text


def test_empty_text(tokenizer):
    tokens, spaces = tokenizer('    ')
    assert tokens == []
    assert spaces == []
