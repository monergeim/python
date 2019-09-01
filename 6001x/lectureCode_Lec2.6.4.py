# Lec 2.6, slide 4

x = 6

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

_________________________________________
s = 'livsmkjposxlikdyhc'
alph = 'abcdefghijklmnopqrstuvwxyz'
ca = 0
i = 0
prev_ca = 0
string = ""
m_str = ""
while i <= (len(s) - 1):
    print "i = %s" % i
    while ca <= (len(alph) - 1):
        print alph[ca]
        if s[i] == alph[ca] and ca >= prev_ca:
            string = string + s[i]
            prev_ca = ca
            print "break"
            if i != (len(s) - 1):
                break
        ca += 1
    else:
        print "String: %s" % string
        if len(string) > len(m_str):
            m_str = string
        string = s[i]
        ca = 0
        prev_ca = 0
    i += 1

print "Number %s"  % m_str
        
        _____________________________
        s = 'euplhlmrbsdhe'
        def chk_char_num(char):
            alph = 'abcdefghijklmnopqrstuvwxyz'
            for cn in range(0,len(alph) - 1):
                if char == alph[cn]:
                    return cn
        pr_n = 0
        string = ''
        mstr = ''
        for i in s:
            print i
            print pr_n
            if chk_char_num(i) >= pr_n:
                string = string + i
            else:
                string = i
            print string
            pr_n = chk_char_num(i)
            if len(string) > len(mstr):
                mstr = string
        print "Number %s"  % mstr