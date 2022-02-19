mysp = __import__("my-voice-analysis")

path = r"./test_data/MLK_Something_happening.wav"

df = mysp.get_df(path)

mysp.mysptotal(path, df=df)
mysp.myspgend(path, df=df)
mysp.myspsyl(path, df=df)
mysp.mysppaus(path, df=df)
mysp.myspsr(path, df=df)
mysp.myspatc(path, df=df)
mysp.myspst(path, df=df)
mysp.myspod(path, df=df)
mysp.myspbala(path, df=df)
mysp.myspf0mean(path, df=df)
mysp.myspf0sd(path, df=df)
mysp.myspf0med(path, df=df)
mysp.myspf0min(path, df=df)
mysp.myspf0max(path, df=df)
mysp.myspf0q25(path, df=df)
mysp.myspf0q75(path, df=df)
mysp.mysppron(path, df=df)
