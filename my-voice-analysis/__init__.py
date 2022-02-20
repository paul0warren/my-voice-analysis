import sys

import pkg_resources
from parselmouth import PraatError

from parselmouth.praat import run_file
import pandas as pd
import numpy as np
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
import os


def get_praat_script_path():
    return pkg_resources.resource_filename(__name__, "myspsolution.praat")


def get_praat_result_objects(sound, path):
    sourcerun = get_praat_script_path()
    objects = None
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
    except Exception as ex:
        print(
            "Something went wrong.  Possible issues could be: unclear audio, invalid file path or access permissions:")
        print(ex)

    return objects


def get_df(p):
    sound = os.path.abspath(p)
    path = os.path.dirname(sound)
    praat_objects = get_praat_result_objects(sound, path)
    z1 = str(praat_objects[1])
    z2 = z1.strip().split()
    z3 = np.array(z2)
    z4 = np.array(z3)[np.newaxis]
    z5 = z4.T

    pron_v = float(z2[14])  # will be the floating point number 8.3
    db = binom.rvs(n=10, p=pron_v, size=10000)
    a = np.array(db)
    pron = np.mean(a) * 100 / 10
    gender = get_gender(float(z2[7]), float(z2[8]))

    df = pd.DataFrame(
        [
            ["number_of_syllables", z5[0, :][0], "# of syllables detected"],
            ["number_of_pauses", z5[1, :][0], "# of pauses detected"],
            ["rate_of_speech", z5[2, :][0], "# syllables/sec original duration"],
            ["articulation_rate", z5[3, :][0], "# syllables/sec speaking duration"],
            ["speaking_duration", z5[4, :][0], "# sec only speaking duration without pauses"],
            ["original_duration", z5[5, :][0], "# sec total speaking duration with pauses"],
            ["balance", z5[6, :][0], "# ratio (speaking duration)/(original duration)"],
            ["f0_mean", z5[7, :][0], "# Hz global mean of fundamental frequency distribution"],
            ["f0_std", z5[8, :][0], "# Hz global standard deviation of fundamental frequency distribution"],
            ["f0_median", z5[9, :][0], "# Hz global median of fundamental frequency distribution"],
            ["f0_min", z5[10, :][0], "# Hz global minimum of fundamental frequency distribution"],
            ["f0_max", z5[11, :][0], "# Hz global maximum of fundamental frequency distribution"],
            ["f0_quantile25", z5[12, :][0], "# Hz global 25th quantile of fundamental frequency distribution"],
            ["f0_quan75", z5[13, :][0], "# Hz global 75th quantile of fundamental frequency distribution"],
            ["pron", pron, "Pronunciation_posteriori_probability_score_percentage"],
            ["gender", gender, "Estimated gender"]
        ],
        columns=["metric", "value", "description"])
    return df


def get_value_for_metric(df, metric):
    value = "NA"
    try:
        value = df.loc[df["metric"] == metric].iloc[0]['value']
    except Exception as ex:
        print("Problem getting " + metric + " from the dataframe:")
        print(ex)
    return value


def get_gender(y, z):
    if y <= 114:
        g = 101
        j = 3.4
    elif 114 < y <= 135:
        g = 128
        j = 4.35
    elif 135 < y <= 163:
        g = 142
        j = 4.85
    elif 163 < y <= 197:
        g = 182
        j = 2.7
    elif 197 < y <= 226:
        g = 213
        j = 4.5
    elif y > 226:
        g = 239
        j = 5.3
    else:
        return "Voice not recognized"

    def teset(a, b, c, d):
        d1 = np.random.wald(a, 1, 1000)
        d2 = np.random.wald(b, 1, 1000)
        d3 = ks_2samp(d1, d2)
        c1 = np.random.normal(a, c, 1000)
        c2 = np.random.normal(b, d, 1000)
        c3 = ttest_ind(c1, c2)
        y = ([d3[0], d3[1], abs(c3[0]), c3[1]])
        return y

    nn = 0
    mm = teset(g, j, y, z)
    while mm[3] > 0.05 and mm[0] > 0.04 or nn < 5:
        mm = teset(g, j, y, z)
        nn = nn + 1
    nnn = nn
    if mm[3] <= 0.09:
        mmm = mm[3]
    else:
        mmm = 0.35
    if 97 < y <= 114:
        return "a Male, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % mmm, nnn
    elif 114 < y <= 135:
        return "a Male, mood of speech: Reading, p-value/sample size= :%.2f" % mmm, nnn
    elif 135 < y <= 163:
        return "a Male, mood of speech: speaking passionately, p-value/sample size= :%.2f" % mmm, nnn
    elif 163 < y <= 197:
        return "a female, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % mmm, nnn
    elif 197 < y <= 226:
        return "a female, mood of speech: Reading, p-value/sample size= :%.2f" % mmm, nnn
    elif 226 < y <= 245:
        return "a female, mood of speech: speaking passionately, p-value/sample size= :%.2f" % mmm, nnn
    else:
        return "Voice not recognized"


# ORIGINAL LIBRARY METHODS PRESERVED FOR BACKWARDS COMPATIBILITY
# Params are different now.  Only need the full path to the audio file (including .wav)
# Optional df param is added to reduce redundant running of PRAAT script (if df is specified, path is ignored)

def myspsyl(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "number_of_syllables")
    print("number_ of_syllables=", value)
    return value


def mysppaus(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "number_of_pauses")
    print("number_of_pauses=", value)
    return value


def myspsr(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "rate_of_speech")
    print("rate_of_speech=", value, "# syllables/sec original duration")
    return value


def myspatc(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "articulation_rate")
    print("articulation_rate=", value, "# syllables/sec speaking duration")
    return value


def myspst(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "speaking_duration")
    print("speaking_duration=", value, "# sec only speaking duration without pauses")
    return value


def myspod(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "original_duration")
    print("original_duration=", value, "# sec total speaking duration with pauses")
    return value


def myspbala(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "balance")
    print("balance=", value, "# ratio (speaking duration)/(original duration)")
    return value


def myspf0mean(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "f0_mean")
    print("f0_mean=", value, "# Hz global mean of fundamental frequency distribution")
    return value


def myspf0sd(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "f0_std")
    print("f0_SD=", value, "# Hz global standard deviation of fundamental frequency distribution")
    return value


def myspf0med(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "f0_median")
    print("f0_MD=", value, "# Hz global median of fundamental frequency distribution")
    return value


def myspf0min(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "f0_min")
    print("f0_min=", value, "# Hz global minimum of fundamental frequency distribution")
    return value


def myspf0max(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "f0_max")
    print("f0_max=", value, "# Hz global maximum of fundamental frequency distribution")
    return value


def myspf0q25(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "f0_quan25")
    print("f0_quan25=", value, "# Hz global 25th quantile of fundamental frequency distribution")
    return value


def myspf0q75(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "f0_quan75")
    print("f0_quan75=", value, "# Hz global 75th quantile of fundamental frequency distribution")
    return value


def mysptotal(p, df=None):
    if df is None:
        df = get_df(p)
    # mysptotal doesn't use pron or gender.  dropping them before printing.
    df = df.iloc[:-2]
    # mysptotal also does not include description column. dropping it before printing
    df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=True)
    df.set_index("metric")
    value = df.to_string(index=False, header=False)
    print(value)
    return value


def myspgend(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "gender")
    if value is not None and value != "NA":
        value = value[0]
    print(value)
    return value


def mysppron(p, df=None):
    if df is None:
        df = get_df(p)
    value = get_value_for_metric(df, "pron")
    print("Pronunciation_posteriori_probability_score_percentage= :%.2f" % value)
    return value
