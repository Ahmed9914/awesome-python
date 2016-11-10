# coding: utf-8

"""
    The approach taken is explained below. I decided to do it simply.
    Initially I was considering parsing the data into some sort of
    structure and then generating an appropriate README. I am still
    considering doing it - but for now this should work. The only issue
    I see is that it only sorts the entries at the lowest level, and that
    the order of the top-level contents do not match the order of the actual
    entries.

    This could be extended by having nested blocks, sorting them recursively
    and flattening the end structure into a list of lines. Revision 2 maybe ^.^.
"""

def sort_alphabetically():
    with open('README.md', 'r') as read_me_file:
        read_me = read_me_file.readlines()
    read_all = ''.join(read_me)
    titles = ''.join(read_all.split('- - -')[0])
    blocks = ''.join(read_all.split('- - -')[1]).split('\n# ')
    
    for i in range(len(blocks)):
       blocks[i] = '#'+blocks[i]+'\n'
         
    inner_blocks = sorted(blocks[0].split('##'))
    
    for i in range(len(inner_blocks)):
        inner_blocks[i]='##'+inner_blocks[i]
        
    inner_blocks=''.join(inner_blocks)
    blocks[0] = inner_blocks
    final = titles + ''.join(blocks)
    
    with open('README.md', 'w+') as sorted_file:
        sorted_file.write(final)

def main():
    # First, we load the current README into memory as an array of lines
    with open('README.md', 'r') as read_me_file:
        read_me = read_me_file.readlines()

    # Then we cluster the lines together as blocks
    # Each block represents a collection of lines that should be sorted
    # This was done by assuming only links ([...](...)) are meant to be sorted
    # Clustering is done by indentation
    blocks = []
    last_indent = None
    for line in read_me:
        s_line = line.lstrip()
        indent = len(line) - len(s_line)

        if any([s_line.startswith(s) for s in ['* [', '- [']]):
            if indent == last_indent:
                blocks[-1].append(line)
            else:
                blocks.append([line])
            last_indent = indent
        else:
            blocks.append([line])
            last_indent = None

    with open('README.md', 'w+') as sorted_file:
        # Then all of the blocks are sorted individually
        blocks = [''.join(sorted(block, key=lambda s: s.lower())) for block in blocks]
        # And the result is written back to README.md
        sorted_file.write(''.join(blocks))

    # Then we make the alphabetical sorting
    sort_alphabetically()

if __name__ == "__main__":
    main()
