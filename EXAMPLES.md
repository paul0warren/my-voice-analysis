# My-Voice Analysis

## Example usage

### Gender recognition and mood of speech: Function *myspgend(p)*

Code:

    mysp=__import__("my-voice-analysis")

    p="./test_data/MLK_Something_happening.wav" # Audio File

    mysp.myspgend(p)

Output:
> a female, mood of speech: Reading, p-value/sample size= :0.00 5

### Pronunciation posteriori probability score percentage: Function *mysppron(p)*

Code:

    mysp=__import__("my-voice-analysis")

    p="./test_data/MLK_Something_happening.wav" # Audio File

    mysp.mysppron(p)

Output:

>Pronunciation_posteriori_probability_score_percentage= :85.00

### Detect and count number of syllables: Function *myspsyl(p)*

Code:

    mysp=__import__("my-voice-analysis")

    p="./test_data/MLK_Something_happening.wav" # Audio File

    mysp.myspsyl(p)

Output:

>number_of_syllables= 154

### Detect and count number of fillers and pauses: Function *mysppaus(p)*

Code:

    mysp=__import__("my-voice-analysis")

    p="./test_data/MLK_Something_happening.wav" # Audio File

    mysp.mysppaus(p)

Output:

>number_of_pauses= 22


### Measure the rate of speech (speed): Function *myspsr(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspsr(p)

Output:

>rate_of_speech= 3 # syllables/sec original duration

### Measure the articulation (speed): Function *myspatc(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspatc(p)

Output:

>articulation_rate= 5 # syllables/sec speaking duration

### Measure speaking time (excl. fillers and pause): Function *myspst(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspst(p)

Output:

>speaking_duration= 31.6 # sec only speaking duration without pauses

### Measure total speaking duration (inc. fillers and pauses): Function *myspod(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspod(p)

Output:

>original_duration= 49.2 # sec total speaking duration with pauses

### Measure ratio between speaking duration and total speaking duration: Function *myspbala(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspbala(p)

Output:

>balance= 0.6 # ratio (speaking duration)/(original duration)

### Measure fundamental frequency distribution mean: Function *myspf0mean(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspf0mean(p)

Output:

>f0_mean= 212.45 # Hz global mean of fundamental frequency distribution

### Measure fundamental frequency distribution SD: Function *myspf0sd(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspf0sd(p)

Output:

>f0_SD= 57.85 # Hz global standard deviation of fundamental frequency distribution

### Measure fundamental frequency distribution median: Function *myspf0med(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspf0med(p)

Output:

>f0_MD= 205.7 # Hz global median of fundamental frequency distribution




### Measure fundamental frequency distribution minimum: Function *myspf0min(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspf0min(p)

Output:

>f0_min= 77 # Hz global minimum of fundamental frequency distribution

### Measure fundamental frequency distribution maximum: Function *myspf0max(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspf0max(p)

Output:

>f0_max= 414 # Hz global maximum of fundamental frequency distribution

### Measure 25th quantile fundamental frequency distribution: Function *myspf0q25(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspf0q25(p)

Output:

>f0_quan25= 171 # Hz global 25th quantile of fundamental frequency distribution

### Measure 75th quantile fundamental frequency distribution: Function *myspf0q75(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.myspf0q75(p)

Output:

>f0_quan75= 244 # Hz global 75th quantile of fundamental frequency distribution




### Overview: Function *mysptotal(p)*

Code:

    mysp=__import__("my-voice-analysis")
    
    p="./test_data/MLK_Something_happening.wav" # Audio File
    
    mysp.mysptotal(p)



Output:

|  |  |
| ----------- | ----------- |
|number_ of_syllables  |   154
|number_of_pauses     |     22
|rate_of_speech      |       3
|articulation_rate    |      5
|speaking_duration   |    31.6
|original_duration    |   49.2
|balance       |           0.6
|f0_mean       |        212.45
|f0_std        |         57.85
|f0_median      |        205.7
|f0_min         |           77
|f0_max          |         414
|f0_quantile25     |       171
|f0_quan75        |        244




**Development**

The following is a fork of the original repository:

https://github.com/Shahabks/my-voice-analysis

[Paul Warren](https://github.com/paul0warren) on behalf of 
[ECSC, ltd](https://github.com/ecscstatsconsulting) has made 
some modifications to make it easier to import this library 
in to other Python Projects. Also some minor changes have 
been made to the original parameters and code structure to 
improve performance and usability, but the underlying PRAAT 
script logic is the same.

