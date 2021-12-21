def main():
    tokens_file = open('tokens.txt', 'r')
    tokens = tokens_file.readlines()

    if len(tokens) == 0:
        print('> ERROR: No tokens in the "tokens.txt" file !')
        return

    with open('result.txt', 'w') as w:
        w.write("")
        w.close()

    for token in tokens:
        with open('result.txt', 'a') as f:
            f.write(token.split(":")[2])
            f.close()

    input('Finished ! Your tokens were exported into the "result.txt" file.')

main()