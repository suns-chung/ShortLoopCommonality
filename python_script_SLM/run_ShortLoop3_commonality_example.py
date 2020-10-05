exec(open('find_shortloopcommonality.py').read())
CMLdic=process_loop2adjset('CML_ShortLoop3.dat')
CMLpairs=process_loop2pairs('CML_ShortLoop3.dat')
find_ShortLoopCommonality(CMLdic,CMLpairs,'CML_ShortLoopCommonality_95_stringent.dat',0.95)
