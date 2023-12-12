import pandas as pd
df = pd.read_csv(r'nba_PositionCleaned.csv')

class Format:
    end = '\033[0m'
    underline = '\033[4m'

#C, PF, PG, SF, SG

positions = ["C", "PF", "PG", "SF", "SG"]
statistics = ["mean", "mode", "median", "range", "std", "var"]

# SALARY
print(Format.underline + "\nSALARY\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "Salary"].mean()   # Center Salary mean
mean2 = df.loc[df["Position"] == "PF", "Salary"].mean()  # Power Forward Salary mean
mean3 = df.loc[df["Position"] == "PG", "Salary"].mean()  # Point Guard Salary mean
mean4 = df.loc[df["Position"] == "SF", "Salary"].mean()  # Small Forward Salary mean
mean5 = df.loc[df["Position"] == "SG", "Salary"].mean()  # Shooting Guard Salary mean

mode1 = df.loc[df["Position"] == "C", "Salary"].mode()   # Center Salary mode
mode2 = df.loc[df["Position"] == "PF", "Salary"].mode()  # Power Forward Salary mode
mode3 = df.loc[df["Position"] == "PG", "Salary"].mode()  # Point Guard Salary mode
mode4 = df.loc[df["Position"] == "SF", "Salary"].mode()  # Small Forward Salary mode
mode5 = df.loc[df["Position"] == "SG", "Salary"].mode()  # Shooting Guard Salary mode

median1 = df.loc[df["Position"] == "C", "Salary"].median()  # Center Salary median
median2 = df.loc[df["Position"] == "PF", "Salary"].median() # Power Forward Salary median
median3 = df.loc[df["Position"] == "PG", "Salary"].median() # Point Guard Salary median
median4 = df.loc[df["Position"] == "SF", "Salary"].median() # Small Forward Salary median
median5 = df.loc[df["Position"] == "SG", "Salary"].median() # Shooting Guard Salary median

range1 = max(df.loc[df["Position"] == "C", "Salary"]) - min(df.loc[df["Position"] == "C", "Salary"])   # Center Salary range
range2 = max(df.loc[df["Position"] == "PF", "Salary"]) - min(df.loc[df["Position"] == "PF", "Salary"]) # Power Forward Salary range
range3 = max(df.loc[df["Position"] == "PG", "Salary"]) - min(df.loc[df["Position"] == "PG", "Salary"]) # Point Guard Salary range
range4 = max(df.loc[df["Position"] == "SF", "Salary"]) - min(df.loc[df["Position"] == "SF", "Salary"]) # Small Forward Salary range
range5 = max(df.loc[df["Position"] == "SG", "Salary"]) - min(df.loc[df["Position"] == "SF", "Salary"]) # Shooting Guard Salary range

std1 = df.loc[df["Position"] == "C", "Salary"].std()   # Center Salary std
std2 = df.loc[df["Position"] == "PF", "Salary"].std()  # Power Forward Salary std
std3 = df.loc[df["Position"] == "PG", "Salary"].std()  # Point Guard Salary std
std4 = df.loc[df["Position"] == "SF", "Salary"].std()  # Small Forward Salary std
std5 = df.loc[df["Position"] == "SG", "Salary"].std()  # Shooting Guard Salary std

var1 = df.loc[df["Position"] == "C", "Salary"].var()  # Center Salary variance
var2 = df.loc[df["Position"] == "PF", "Salary"].var() # Power Forward Salary variance
var3 = df.loc[df["Position"] == "PG", "Salary"].var() # Point Guard Salary variance
var4 = df.loc[df["Position"] == "SF", "Salary"].var() # Small Forward Salary variance
var5 = df.loc[df["Position"] == "SG", "Salary"].var() # Shooting Guard Salary variance

avg1 = df.loc[df["Position"] == "C", "Salary"].sum() / 91   # Center Salary avg
avg2 = df.loc[df["Position"] == "PF", "Salary"].sum() / 86  # Power Forward Salary avg
avg3 = df.loc[df["Position"] == "PG", "Salary"].sum() / 79  # Point Guard Salary avg
avg4 = df.loc[df["Position"] == "SF", "Salary"].sum() / 94  # Small Forward Salary avg
avg5 = df.loc[df["Position"] == "SG", "Salary"].sum() / 117  # Shooting Guard Salary avg

for position in positions:
    print(f"{Format.underline}\n{position} SALARY\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["Salary"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} Salary is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["Salary"].max() if not subset.empty else "N/A"
            minVal = subset["Salary"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} Salary is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["Salary"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} Salary is {meanVal:.2f}")
        else:
            statVal = getattr(subset["Salary"], stat)()
            print(f"The {stat} value of the {position} Salary is {statVal:.2f}")
        print()

# Field Goals Made Per Game
print(Format.underline + "\nField Goals Made Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "FG"].mean()   # Center FG mean
mean2 = df.loc[df["Position"] == "PF", "FG"].mean()  # Power Forward FG mean
mean3 = df.loc[df["Position"] == "PG", "FG"].mean()  # Point Guard FG mean
mean4 = df.loc[df["Position"] == "SF", "FG"].mean()  # Small Forward FG mean
mean5 = df.loc[df["Position"] == "SG", "FG"].mean()  # Shooting Guard FG mean

mode1 = df.loc[df["Position"] == "C", "FG"].mode()   # Center FG mode
mode2 = df.loc[df["Position"] == "PF", "FG"].mode()  # Power Forward FG mode
mode3 = df.loc[df["Position"] == "PG", "FG"].mode()  # Point Guard FG mode
mode4 = df.loc[df["Position"] == "SF", "FG"].mode()  # Small Forward FG mode
mode5 = df.loc[df["Position"] == "SG", "FG"].mode()  # Shooting Guard FG mode

median1 = df.loc[df["Position"] == "C", "FG"].median()  # Center FG median
median2 = df.loc[df["Position"] == "PF", "FG"].median() # Power Forward FG median
median3 = df.loc[df["Position"] == "PG", "FG"].median() # Point Guard FG median
median4 = df.loc[df["Position"] == "SF", "FG"].median() # Small Forward FG median
median5 = df.loc[df["Position"] == "SG", "FG"].median() # Shooting Guard FG median

range1 = max(df.loc[df["Position"] == "C", "FG"]) - min(df.loc[df["Position"] == "C", "FG"])   # Center FG range
range2 = max(df.loc[df["Position"] == "PF", "FG"]) - min(df.loc[df["Position"] == "PF", "FG"]) # Power Forward FG range
range3 = max(df.loc[df["Position"] == "PG", "FG"]) - min(df.loc[df["Position"] == "PG", "FG"]) # Point Guard FG range
range4 = max(df.loc[df["Position"] == "SF", "FG"]) - min(df.loc[df["Position"] == "SF", "FG"]) # Small Forward FG range
range5 = max(df.loc[df["Position"] == "SG", "FG"]) - min(df.loc[df["Position"] == "SF", "FG"]) # Shooting Guard FG range

std1 = df.loc[df["Position"] == "C", "FG"].std()   # Center FG std
std2 = df.loc[df["Position"] == "PF", "FG"].std()  # Power Forward FG std
std3 = df.loc[df["Position"] == "PG", "FG"].std()  # Point Guard FG std
std4 = df.loc[df["Position"] == "SF", "FG"].std()  # Small Forward FG std
std5 = df.loc[df["Position"] == "SG", "FG"].std()  # Shooting Guard FG std

var1 = df.loc[df["Position"] == "C", "FG"].var()  # Center FG variance
var2 = df.loc[df["Position"] == "PF", "FG"].var() # Power Forward FG variance
var3 = df.loc[df["Position"] == "PG", "FG"].var() # Point Guard FG variance
var4 = df.loc[df["Position"] == "SF", "FG"].var() # Small Forward FG variance
var5 = df.loc[df["Position"] == "SG", "FG"].var() # Shooting Guard FG variance

avg1 = df.loc[df["Position"] == "C", "FG"].sum() / 91   # Center FG avg
avg2 = df.loc[df["Position"] == "PF", "FG"].sum() / 86  # Power Forward FG avg
avg3 = df.loc[df["Position"] == "PG", "FG"].sum() / 79  # Point Guard FG avg
avg4 = df.loc[df["Position"] == "SF", "FG"].sum() / 94  # Small Forward FG avg
avg5 = df.loc[df["Position"] == "SG", "FG"].sum() / 117  # Shooting Guard FG avg


for position in positions:
    print(f"{Format.underline}\n{position} FG\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["FG"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} FG is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["FG"].max() if not subset.empty else "N/A"
            minVal = subset["FG"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} FG is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["FG"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} FG is {meanVal:.2f}")
        else:
            statVal = getattr(subset["FG"], stat)()
            print(f"The {stat} value of the {position} FG is {statVal:.2f}")
        print()

# 3 Point FG Made Per Game
print(Format.underline + "\n3 Point FG Made Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "3P"].mean()   # Center 3P mean
mean2 = df.loc[df["Position"] == "PF", "3P"].mean()  # Power Forward 3P mean
mean3 = df.loc[df["Position"] == "PG", "3P"].mean()  # Point Guard 3P mean
mean4 = df.loc[df["Position"] == "SF", "3P"].mean()  # Small Forward 3P mean
mean5 = df.loc[df["Position"] == "SG", "3P"].mean()  # Shooting Guard 3P mean

mode1 = df.loc[df["Position"] == "C", "3P"].mode()   # Center 3P mode
mode2 = df.loc[df["Position"] == "PF", "3P"].mode()  # Power Forward 3P mode
mode3 = df.loc[df["Position"] == "PG", "3P"].mode()  # Point Guard 3P mode
mode4 = df.loc[df["Position"] == "SF", "3P"].mode()  # Small Forward 3P mode
mode5 = df.loc[df["Position"] == "SG", "3P"].mode()  # Shooting Guard 3P mode

median1 = df.loc[df["Position"] == "C", "3P"].median()  # Center 3P median
median2 = df.loc[df["Position"] == "PF", "3P"].median() # Power Forward 3P median
median3 = df.loc[df["Position"] == "PG", "3P"].median() # Point Guard 3P median
median4 = df.loc[df["Position"] == "SF", "3P"].median() # Small Forward 3P median
median5 = df.loc[df["Position"] == "SG", "3P"].median() # Shooting Guard 3P median

range1 = max(df.loc[df["Position"] == "C", "3P"]) - min(df.loc[df["Position"] == "C", "3P"])   # Center 3P range
range2 = max(df.loc[df["Position"] == "PF", "3P"]) - min(df.loc[df["Position"] == "PF", "3P"]) # Power Forward 3P range
range3 = max(df.loc[df["Position"] == "PG", "3P"]) - min(df.loc[df["Position"] == "PG", "3P"]) # Point Guard 3P range
range4 = max(df.loc[df["Position"] == "SF", "3P"]) - min(df.loc[df["Position"] == "SF", "3P"]) # Small Forward 3P range
range5 = max(df.loc[df["Position"] == "SG", "3P"]) - min(df.loc[df["Position"] == "SF", "3P"]) # Shooting Guard 3P range

std1 = df.loc[df["Position"] == "C", "3P"].std()   # Center 3P std
std2 = df.loc[df["Position"] == "PF", "3P"].std()  # Power Forward 3P std
std3 = df.loc[df["Position"] == "PG", "3P"].std()  # Point Guard 3P std
std4 = df.loc[df["Position"] == "SF", "3P"].std()  # Small Forward 3P std
std5 = df.loc[df["Position"] == "SG", "3P"].std()  # Shooting Guard 3P std

var1 = df.loc[df["Position"] == "C", "3P"].var()  # Center 3P variance
var2 = df.loc[df["Position"] == "PF", "3P"].var() # Power Forward 3P variance
var3 = df.loc[df["Position"] == "PG", "3P"].var() # Point Guard 3P variance
var4 = df.loc[df["Position"] == "SF", "3P"].var() # Small Forward 3P variance
var5 = df.loc[df["Position"] == "SG", "3P"].var() # Shooting Guard 3P variance

avg1 = df.loc[df["Position"] == "C", "3P"].sum() / 91   # Center 3P avg
avg2 = df.loc[df["Position"] == "PF", "3P"].sum() / 86  # Power Forward 3P avg
avg3 = df.loc[df["Position"] == "PG", "3P"].sum() / 79  # Point Guard 3P avg
avg4 = df.loc[df["Position"] == "SF", "3P"].sum() / 94  # Small Forward 3P avg
avg5 = df.loc[df["Position"] == "SG", "3P"].sum() / 117  # Shooting Guard 3P avg


for position in positions:
    print(f"{Format.underline}\n{position} 3P\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["3P"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} 3P is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["3P"].max() if not subset.empty else "N/A"
            minVal = subset["3P"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} 3P is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["3P"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} 3P is {meanVal:.2f}")
        else:
            statVal = getattr(subset["3P"], stat)()
            print(f"The {stat} value of the {position} 3P is {statVal:.2f}")
        print()

# 2 Point FG Made Per Game
print(Format.underline + "\n2 Point FG Made Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "2P"].mean()   # Center 2P mean
mean2 = df.loc[df["Position"] == "PF", "2P"].mean()  # Power Forward 2P mean
mean3 = df.loc[df["Position"] == "PG", "2P"].mean()  # Point Guard 2P mean
mean4 = df.loc[df["Position"] == "SF", "2P"].mean()  # Small Forward 2P mean
mean5 = df.loc[df["Position"] == "SG", "2P"].mean()  # Shooting Guard 2P mean

mode1 = df.loc[df["Position"] == "C", "2P"].mode()   # Center 2P mode
mode2 = df.loc[df["Position"] == "PF", "2P"].mode()  # Power Forward 2P mode
mode3 = df.loc[df["Position"] == "PG", "2P"].mode()  # Point Guard 2P mode
mode4 = df.loc[df["Position"] == "SF", "2P"].mode()  # Small Forward 2P mode
mode5 = df.loc[df["Position"] == "SG", "2P"].mode()  # Shooting Guard 2P mode

median1 = df.loc[df["Position"] == "C", "2P"].median()  # Center 2P median
median2 = df.loc[df["Position"] == "PF", "2P"].median() # Power Forward 2P median
median3 = df.loc[df["Position"] == "PG", "2P"].median() # Point Guard 2P median
median4 = df.loc[df["Position"] == "SF", "2P"].median() # Small Forward 2P median
median5 = df.loc[df["Position"] == "SG", "2P"].median() # Shooting Guard 2P median

range1 = max(df.loc[df["Position"] == "C", "2P"]) - min(df.loc[df["Position"] == "C", "2P"])   # Center 2P range
range2 = max(df.loc[df["Position"] == "PF", "2P"]) - min(df.loc[df["Position"] == "PF", "2P"]) # Power Forward 2P range
range3 = max(df.loc[df["Position"] == "PG", "2P"]) - min(df.loc[df["Position"] == "PG", "2P"]) # Point Guard 2P range
range4 = max(df.loc[df["Position"] == "SF", "2P"]) - min(df.loc[df["Position"] == "SF", "2P"]) # Small Forward 2P range
range5 = max(df.loc[df["Position"] == "SG", "2P"]) - min(df.loc[df["Position"] == "SF", "2P"]) # Shooting Guard 2P range

std1 = df.loc[df["Position"] == "C", "2P"].std()   # Center 2P std
std2 = df.loc[df["Position"] == "PF", "2P"].std()  # Power Forward 2P std
std3 = df.loc[df["Position"] == "PG", "2P"].std()  # Point Guard 2P std
std4 = df.loc[df["Position"] == "SF", "2P"].std()  # Small Forward 2P std
std5 = df.loc[df["Position"] == "SG", "2P"].std()  # Shooting Guard 2P std

var1 = df.loc[df["Position"] == "C", "2P"].var()  # Center 2P variance
var2 = df.loc[df["Position"] == "PF", "2P"].var() # Power Forward 2P variance
var3 = df.loc[df["Position"] == "PG", "2P"].var() # Point Guard 2P variance
var4 = df.loc[df["Position"] == "SF", "2P"].var() # Small Forward 2P variance
var5 = df.loc[df["Position"] == "SG", "2P"].var() # Shooting Guard 2P variance

avg1 = df.loc[df["Position"] == "C", "2P"].sum() / 91   # Center 2P avg
avg2 = df.loc[df["Position"] == "PF", "2P"].sum() / 86  # Power Forward 2P avg
avg3 = df.loc[df["Position"] == "PG", "2P"].sum() / 79  # Point Guard 2P avg
avg4 = df.loc[df["Position"] == "SF", "2P"].sum() / 94  # Small Forward 2P avg
avg5 = df.loc[df["Position"] == "SG", "2P"].sum() / 117  # Shooting Guard 2P avg


for position in positions:
    print(f"{Format.underline}\n{position} 2P\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["2P"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} 2P is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["2P"].max() if not subset.empty else "N/A"
            minVal = subset["2P"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} 2P is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["2P"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} 2P is {meanVal:.2f}")
        else:
            statVal = getattr(subset["2P"], stat)()
            print(f"The {stat} value of the {position} 2P is {statVal:.2f}")
        print()

# Free Throws Made Per Game
print(Format.underline + "\nFree Throws Made Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "FT"].mean()   # Center FT mean
mean2 = df.loc[df["Position"] == "PF", "FT"].mean()  # Power Forward FT mean
mean3 = df.loc[df["Position"] == "PG", "FT"].mean()  # Point Guard FT mean
mean4 = df.loc[df["Position"] == "SF", "FT"].mean()  # Small Forward FT mean
mean5 = df.loc[df["Position"] == "SG", "FT"].mean()  # Shooting Guard FT mean

mode1 = df.loc[df["Position"] == "C", "FT"].mode()   # Center FT mode
mode2 = df.loc[df["Position"] == "PF", "FT"].mode()  # Power Forward FT mode
mode3 = df.loc[df["Position"] == "PG", "FT"].mode()  # Point Guard FT mode
mode4 = df.loc[df["Position"] == "SF", "FT"].mode()  # Small Forward FT mode
mode5 = df.loc[df["Position"] == "SG", "FT"].mode()  # Shooting Guard FT mode

median1 = df.loc[df["Position"] == "C", "FT"].median()  # Center FT median
median2 = df.loc[df["Position"] == "PF", "FT"].median() # Power Forward FT median
median3 = df.loc[df["Position"] == "PG", "FT"].median() # Point Guard FT median
median4 = df.loc[df["Position"] == "SF", "FT"].median() # Small Forward FT median
median5 = df.loc[df["Position"] == "SG", "FT"].median() # Shooting Guard FT median

range1 = max(df.loc[df["Position"] == "C", "FT"]) - min(df.loc[df["Position"] == "C", "FT"])   # Center FT range
range2 = max(df.loc[df["Position"] == "PF", "FT"]) - min(df.loc[df["Position"] == "PF", "FT"]) # Power Forward FT range
range3 = max(df.loc[df["Position"] == "PG", "FT"]) - min(df.loc[df["Position"] == "PG", "FT"]) # Point Guard FT range
range4 = max(df.loc[df["Position"] == "SF", "FT"]) - min(df.loc[df["Position"] == "SF", "FT"]) # Small Forward FT range
range5 = max(df.loc[df["Position"] == "SG", "FT"]) - min(df.loc[df["Position"] == "SF", "FT"]) # Shooting Guard FT range

std1 = df.loc[df["Position"] == "C", "FT"].std()   # Center FT std
std2 = df.loc[df["Position"] == "PF", "FT"].std()  # Power Forward FT std
std3 = df.loc[df["Position"] == "PG", "FT"].std()  # Point Guard FT std
std4 = df.loc[df["Position"] == "SF", "FT"].std()  # Small Forward FT std
std5 = df.loc[df["Position"] == "SG", "FT"].std()  # Shooting Guard FT std

var1 = df.loc[df["Position"] == "C", "FT"].var()  # Center FT variance
var2 = df.loc[df["Position"] == "PF", "FT"].var() # Power Forward FT variance
var3 = df.loc[df["Position"] == "PG", "FT"].var() # Point Guard FT variance
var4 = df.loc[df["Position"] == "SF", "FT"].var() # Small Forward FT variance
var5 = df.loc[df["Position"] == "SG", "FT"].var() # Shooting Guard FT variance

avg1 = df.loc[df["Position"] == "C", "FT"].sum() / 91   # Center FT avg
avg2 = df.loc[df["Position"] == "PF", "FT"].sum() / 86  # Power Forward FT avg
avg3 = df.loc[df["Position"] == "PG", "FT"].sum() / 79  # Point Guard FT avg
avg4 = df.loc[df["Position"] == "SF", "FT"].sum() / 94  # Small Forward FT avg
avg5 = df.loc[df["Position"] == "SG", "FT"].sum() / 117  # Shooting Guard FT avg


for position in positions:
    print(f"{Format.underline}\n{position} FT\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["FT"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} FT is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["FT"].max() if not subset.empty else "N/A"
            minVal = subset["FT"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} FT is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["FT"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} FT is {meanVal:.2f}")
        else:
            statVal = getattr(subset["FT"], stat)()
            print(f"The {stat} value of the {position} FT is {statVal:.2f}")
        print()

# Total Rebounds Per Game
print(Format.underline + "\nTotal Rebounds Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "TRB"].mean()   # Center TRB mean
mean2 = df.loc[df["Position"] == "PF", "TRB"].mean()  # Power Forward TRB mean
mean3 = df.loc[df["Position"] == "PG", "TRB"].mean()  # Point Guard TRB mean
mean4 = df.loc[df["Position"] == "SF", "TRB"].mean()  # Small Forward TRB mean
mean5 = df.loc[df["Position"] == "SG", "TRB"].mean()  # Shooting Guard TRB mean

mode1 = df.loc[df["Position"] == "C", "TRB"].mode()   # Center TRB mode
mode2 = df.loc[df["Position"] == "PF", "TRB"].mode()  # Power Forward TRB mode
mode3 = df.loc[df["Position"] == "PG", "TRB"].mode()  # Point Guard TRB mode
mode4 = df.loc[df["Position"] == "SF", "TRB"].mode()  # Small Forward TRB mode
mode5 = df.loc[df["Position"] == "SG", "TRB"].mode()  # Shooting Guard TRB mode

median1 = df.loc[df["Position"] == "C", "TRB"].median()  # Center TRB median
median2 = df.loc[df["Position"] == "PF", "TRB"].median() # Power Forward TRB median
median3 = df.loc[df["Position"] == "PG", "TRB"].median() # Point Guard TRB median
median4 = df.loc[df["Position"] == "SF", "TRB"].median() # Small Forward TRB median
median5 = df.loc[df["Position"] == "SG", "TRB"].median() # Shooting Guard TRB median

range1 = max(df.loc[df["Position"] == "C", "TRB"]) - min(df.loc[df["Position"] == "C", "TRB"])   # Center TRB range
range2 = max(df.loc[df["Position"] == "PF", "TRB"]) - min(df.loc[df["Position"] == "PF", "TRB"]) # Power Forward TRB range
range3 = max(df.loc[df["Position"] == "PG", "TRB"]) - min(df.loc[df["Position"] == "PG", "TRB"]) # Point Guard TRB range
range4 = max(df.loc[df["Position"] == "SF", "TRB"]) - min(df.loc[df["Position"] == "SF", "TRB"]) # Small Forward TRB range
range5 = max(df.loc[df["Position"] == "SG", "TRB"]) - min(df.loc[df["Position"] == "SF", "TRB"]) # Shooting Guard TRB range

std1 = df.loc[df["Position"] == "C", "TRB"].std()   # Center TRB std
std2 = df.loc[df["Position"] == "PF", "TRB"].std()  # Power Forward TRB std
std3 = df.loc[df["Position"] == "PG", "TRB"].std()  # Point Guard TRB std
std4 = df.loc[df["Position"] == "SF", "TRB"].std()  # Small Forward TRB std
std5 = df.loc[df["Position"] == "SG", "TRB"].std()  # Shooting Guard TRB std

var1 = df.loc[df["Position"] == "C", "TRB"].var()  # Center TRB variance
var2 = df.loc[df["Position"] == "PF", "TRB"].var() # Power Forward TRB variance
var3 = df.loc[df["Position"] == "PG", "TRB"].var() # Point Guard TRB variance
var4 = df.loc[df["Position"] == "SF", "TRB"].var() # Small Forward TRB variance
var5 = df.loc[df["Position"] == "SG", "TRB"].var() # Shooting Guard TRB variance

avg1 = df.loc[df["Position"] == "C", "TRB"].sum() / 91   # Center TRB avg
avg2 = df.loc[df["Position"] == "PF", "TRB"].sum() / 86  # Power Forward TRB avg
avg3 = df.loc[df["Position"] == "PG", "TRB"].sum() / 79  # Point Guard TRB avg
avg4 = df.loc[df["Position"] == "SF", "TRB"].sum() / 94  # Small Forward TRB avg
avg5 = df.loc[df["Position"] == "SG", "TRB"].sum() / 117  # Shooting Guard TRB avg


for position in positions:
    print(f"{Format.underline}\n{position} TRB\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["TRB"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} TRB is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["TRB"].max() if not subset.empty else "N/A"
            minVal = subset["TRB"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} TRB is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["TRB"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} TRB is {meanVal:.2f}")
        else:
            statVal = getattr(subset["TRB"], stat)()
            print(f"The {stat} value of the {position} TRB is {statVal:.2f}")
        print()

# Assists Per Game
print(Format.underline + "\nAssists Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "AST"].mean()   # Center AST mean
mean2 = df.loc[df["Position"] == "PF", "AST"].mean()  # Power Forward AST mean
mean3 = df.loc[df["Position"] == "PG", "AST"].mean()  # Point Guard AST mean
mean4 = df.loc[df["Position"] == "SF", "AST"].mean()  # Small Forward AST mean
mean5 = df.loc[df["Position"] == "SG", "AST"].mean()  # Shooting Guard AST mean

mode1 = df.loc[df["Position"] == "C", "AST"].mode()   # Center AST mode
mode2 = df.loc[df["Position"] == "PF", "AST"].mode()  # Power Forward AST mode
mode3 = df.loc[df["Position"] == "PG", "AST"].mode()  # Point Guard AST mode
mode4 = df.loc[df["Position"] == "SF", "AST"].mode()  # Small Forward AST mode
mode5 = df.loc[df["Position"] == "SG", "AST"].mode()  # Shooting Guard AST mode

median1 = df.loc[df["Position"] == "C", "AST"].median()  # Center AST median
median2 = df.loc[df["Position"] == "PF", "AST"].median() # Power Forward AST median
median3 = df.loc[df["Position"] == "PG", "AST"].median() # Point Guard AST median
median4 = df.loc[df["Position"] == "SF", "AST"].median() # Small Forward AST median
median5 = df.loc[df["Position"] == "SG", "AST"].median() # Shooting Guard AST median

range1 = max(df.loc[df["Position"] == "C", "AST"]) - min(df.loc[df["Position"] == "C", "AST"])   # Center AST range
range2 = max(df.loc[df["Position"] == "PF", "AST"]) - min(df.loc[df["Position"] == "PF", "AST"]) # Power Forward AST range
range3 = max(df.loc[df["Position"] == "PG", "AST"]) - min(df.loc[df["Position"] == "PG", "AST"]) # Point Guard AST range
range4 = max(df.loc[df["Position"] == "SF", "AST"]) - min(df.loc[df["Position"] == "SF", "AST"]) # Small Forward AST range
range5 = max(df.loc[df["Position"] == "SG", "AST"]) - min(df.loc[df["Position"] == "SF", "AST"]) # Shooting Guard AST range

std1 = df.loc[df["Position"] == "C", "AST"].std()   # Center AST std
std2 = df.loc[df["Position"] == "PF", "AST"].std()  # Power Forward AST std
std3 = df.loc[df["Position"] == "PG", "AST"].std()  # Point Guard AST std
std4 = df.loc[df["Position"] == "SF", "AST"].std()  # Small Forward AST std
std5 = df.loc[df["Position"] == "SG", "AST"].std()  # Shooting Guard AST std

var1 = df.loc[df["Position"] == "C", "AST"].var()  # Center AST variance
var2 = df.loc[df["Position"] == "PF", "AST"].var() # Power Forward AST variance
var3 = df.loc[df["Position"] == "PG", "AST"].var() # Point Guard AST variance
var4 = df.loc[df["Position"] == "SF", "AST"].var() # Small Forward AST variance
var5 = df.loc[df["Position"] == "SG", "AST"].var() # Shooting Guard AST variance

avg1 = df.loc[df["Position"] == "C", "AST"].sum() / 91   # Center AST avg
avg2 = df.loc[df["Position"] == "PF", "AST"].sum() / 86  # Power Forward AST avg
avg3 = df.loc[df["Position"] == "PG", "AST"].sum() / 79  # Point Guard AST avg
avg4 = df.loc[df["Position"] == "SF", "AST"].sum() / 94  # Small Forward AST avg
avg5 = df.loc[df["Position"] == "SG", "AST"].sum() / 117  # Shooting Guard AST avg


for position in positions:
    print(f"{Format.underline}\n{position} AST\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["AST"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} AST is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["AST"].max() if not subset.empty else "N/A"
            minVal = subset["AST"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} AST is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["AST"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} AST is {meanVal:.2f}")
        else:
            statVal = getattr(subset["AST"], stat)()
            print(f"The {stat} value of the {position} AST is {statVal:.2f}")
        print()

# Steals Per Game
print(Format.underline + "\nSteals Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "STL"].mean()   # Center STL mean
mean2 = df.loc[df["Position"] == "PF", "STL"].mean()  # Power Forward STL mean
mean3 = df.loc[df["Position"] == "PG", "STL"].mean()  # Point Guard STL mean
mean4 = df.loc[df["Position"] == "SF", "STL"].mean()  # Small Forward STL mean
mean5 = df.loc[df["Position"] == "SG", "STL"].mean()  # Shooting Guard STL mean

mode1 = df.loc[df["Position"] == "C", "STL"].mode()   # Center STL mode
mode2 = df.loc[df["Position"] == "PF", "STL"].mode()  # Power Forward STL mode
mode3 = df.loc[df["Position"] == "PG", "STL"].mode()  # Point Guard STL mode
mode4 = df.loc[df["Position"] == "SF", "STL"].mode()  # Small Forward STL mode
mode5 = df.loc[df["Position"] == "SG", "STL"].mode()  # Shooting Guard STL mode

median1 = df.loc[df["Position"] == "C", "STL"].median()  # Center STL median
median2 = df.loc[df["Position"] == "PF", "STL"].median() # Power Forward STL median
median3 = df.loc[df["Position"] == "PG", "STL"].median() # Point Guard STL median
median4 = df.loc[df["Position"] == "SF", "STL"].median() # Small Forward STL median
median5 = df.loc[df["Position"] == "SG", "STL"].median() # Shooting Guard STL median

range1 = max(df.loc[df["Position"] == "C", "STL"]) - min(df.loc[df["Position"] == "C", "STL"])   # Center STL range
range2 = max(df.loc[df["Position"] == "PF", "STL"]) - min(df.loc[df["Position"] == "PF", "STL"]) # Power Forward STL range
range3 = max(df.loc[df["Position"] == "PG", "STL"]) - min(df.loc[df["Position"] == "PG", "STL"]) # Point Guard STL range
range4 = max(df.loc[df["Position"] == "SF", "STL"]) - min(df.loc[df["Position"] == "SF", "STL"]) # Small Forward STL range
range5 = max(df.loc[df["Position"] == "SG", "STL"]) - min(df.loc[df["Position"] == "SF", "STL"]) # Shooting Guard STL range

std1 = df.loc[df["Position"] == "C", "STL"].std()   # Center STL std
std2 = df.loc[df["Position"] == "PF", "STL"].std()  # Power Forward STL std
std3 = df.loc[df["Position"] == "PG", "STL"].std()  # Point Guard STL std
std4 = df.loc[df["Position"] == "SF", "STL"].std()  # Small Forward STL std
std5 = df.loc[df["Position"] == "SG", "STL"].std()  # Shooting Guard STL std

var1 = df.loc[df["Position"] == "C", "STL"].var()  # Center STL variance
var2 = df.loc[df["Position"] == "PF", "STL"].var() # Power Forward STL variance
var3 = df.loc[df["Position"] == "PG", "STL"].var() # Point Guard STL variance
var4 = df.loc[df["Position"] == "SF", "STL"].var() # Small Forward STL variance
var5 = df.loc[df["Position"] == "SG", "STL"].var() # Shooting Guard STL variance

avg1 = df.loc[df["Position"] == "C", "STL"].sum() / 91   # Center STL avg
avg2 = df.loc[df["Position"] == "PF", "STL"].sum() / 86  # Power Forward STL avg
avg3 = df.loc[df["Position"] == "PG", "STL"].sum() / 79  # Point Guard STL avg
avg4 = df.loc[df["Position"] == "SF", "STL"].sum() / 94  # Small Forward STL avg
avg5 = df.loc[df["Position"] == "SG", "STL"].sum() / 117  # Shooting Guard STL avg


for position in positions:
    print(f"{Format.underline}\n{position} STL\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["STL"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} STL is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["STL"].max() if not subset.empty else "N/A"
            minVal = subset["STL"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} STL is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["STL"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} STL is {meanVal:.2f}")
        else:
            statVal = getattr(subset["STL"], stat)()
            print(f"The {stat} value of the {position} STL is {statVal:.2f}")
        print()

# Blocks Per Game
print(Format.underline + "\nBlocks Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "BLK"].mean()   # Center BLK mean
mean2 = df.loc[df["Position"] == "PF", "BLK"].mean()  # Power Forward BLK mean
mean3 = df.loc[df["Position"] == "PG", "BLK"].mean()  # Point Guard BLK mean
mean4 = df.loc[df["Position"] == "SF", "BLK"].mean()  # Small Forward BLK mean
mean5 = df.loc[df["Position"] == "SG", "BLK"].mean()  # Shooting Guard BLK mean

mode1 = df.loc[df["Position"] == "C", "BLK"].mode()   # Center BLK mode
mode2 = df.loc[df["Position"] == "PF", "BLK"].mode()  # Power Forward BLK mode
mode3 = df.loc[df["Position"] == "PG", "BLK"].mode()  # Point Guard BLK mode
mode4 = df.loc[df["Position"] == "SF", "BLK"].mode()  # Small Forward BLK mode
mode5 = df.loc[df["Position"] == "SG", "BLK"].mode()  # Shooting Guard BLK mode

median1 = df.loc[df["Position"] == "C", "BLK"].median()  # Center BLK median
median2 = df.loc[df["Position"] == "PF", "BLK"].median() # Power Forward BLK median
median3 = df.loc[df["Position"] == "PG", "BLK"].median() # Point Guard BLK median
median4 = df.loc[df["Position"] == "SF", "BLK"].median() # Small Forward BLK median
median5 = df.loc[df["Position"] == "SG", "BLK"].median() # Shooting Guard BLK median

range1 = max(df.loc[df["Position"] == "C", "BLK"]) - min(df.loc[df["Position"] == "C", "BLK"])   # Center BLK range
range2 = max(df.loc[df["Position"] == "PF", "BLK"]) - min(df.loc[df["Position"] == "PF", "BLK"]) # Power Forward BLK range
range3 = max(df.loc[df["Position"] == "PG", "BLK"]) - min(df.loc[df["Position"] == "PG", "BLK"]) # Point Guard BLK range
range4 = max(df.loc[df["Position"] == "SF", "BLK"]) - min(df.loc[df["Position"] == "SF", "BLK"]) # Small Forward BLK range
range5 = max(df.loc[df["Position"] == "SG", "BLK"]) - min(df.loc[df["Position"] == "SF", "BLK"]) # Shooting Guard BLK range

std1 = df.loc[df["Position"] == "C", "BLK"].std()   # Center BLK std
std2 = df.loc[df["Position"] == "PF", "BLK"].std()  # Power Forward BLK std
std3 = df.loc[df["Position"] == "PG", "BLK"].std()  # Point Guard BLK std
std4 = df.loc[df["Position"] == "SF", "BLK"].std()  # Small Forward BLK std
std5 = df.loc[df["Position"] == "SG", "BLK"].std()  # Shooting Guard BLK std

var1 = df.loc[df["Position"] == "C", "BLK"].var()  # Center BLK variance
var2 = df.loc[df["Position"] == "PF", "BLK"].var() # Power Forward BLK variance
var3 = df.loc[df["Position"] == "PG", "BLK"].var() # Point Guard BLK variance
var4 = df.loc[df["Position"] == "SF", "BLK"].var() # Small Forward BLK variance
var5 = df.loc[df["Position"] == "SG", "BLK"].var() # Shooting Guard BLK variance

avg1 = df.loc[df["Position"] == "C", "BLK"].sum() / 91   # Center BLK avg
avg2 = df.loc[df["Position"] == "PF", "BLK"].sum() / 86  # Power Forward BLK avg
avg3 = df.loc[df["Position"] == "PG", "BLK"].sum() / 79  # Point Guard BLK avg
avg4 = df.loc[df["Position"] == "SF", "BLK"].sum() / 94  # Small Forward BLK avg
avg5 = df.loc[df["Position"] == "SG", "BLK"].sum() / 117  # Shooting Guard BLK avg


for position in positions:
    print(f"{Format.underline}\n{position} BLK\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["BLK"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} BLK is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["BLK"].max() if not subset.empty else "N/A"
            minVal = subset["BLK"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} BLK is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["BLK"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} BLK is {meanVal:.2f}")
        else:
            statVal = getattr(subset["BLK"], stat)()
            print(f"The {stat} value of the {position} BLK is {statVal:.2f}")
        print()

# Turnovers Per Game
print(Format.underline + "\nTurnovers Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "TOV"].mean()   # Center TOV mean
mean2 = df.loc[df["Position"] == "PF", "TOV"].mean()  # Power Forward TOV mean
mean3 = df.loc[df["Position"] == "PG", "TOV"].mean()  # Point Guard TOV mean
mean4 = df.loc[df["Position"] == "SF", "TOV"].mean()  # Small Forward TOV mean
mean5 = df.loc[df["Position"] == "SG", "TOV"].mean()  # Shooting Guard TOV mean

mode1 = df.loc[df["Position"] == "C", "TOV"].mode()   # Center TOV mode
mode2 = df.loc[df["Position"] == "PF", "TOV"].mode()  # Power Forward TOV mode
mode3 = df.loc[df["Position"] == "PG", "TOV"].mode()  # Point Guard TOV mode
mode4 = df.loc[df["Position"] == "SF", "TOV"].mode()  # Small Forward TOV mode
mode5 = df.loc[df["Position"] == "SG", "TOV"].mode()  # Shooting Guard TOV mode

median1 = df.loc[df["Position"] == "C", "TOV"].median()  # Center TOV median
median2 = df.loc[df["Position"] == "PF", "TOV"].median() # Power Forward TOV median
median3 = df.loc[df["Position"] == "PG", "TOV"].median() # Point Guard TOV median
median4 = df.loc[df["Position"] == "SF", "TOV"].median() # Small Forward TOV median
median5 = df.loc[df["Position"] == "SG", "TOV"].median() # Shooting Guard TOV median

range1 = max(df.loc[df["Position"] == "C", "TOV"]) - min(df.loc[df["Position"] == "C", "TOV"])   # Center TOV range
range2 = max(df.loc[df["Position"] == "PF", "TOV"]) - min(df.loc[df["Position"] == "PF", "TOV"]) # Power Forward TOV range
range3 = max(df.loc[df["Position"] == "PG", "TOV"]) - min(df.loc[df["Position"] == "PG", "TOV"]) # Point Guard TOV range
range4 = max(df.loc[df["Position"] == "SF", "TOV"]) - min(df.loc[df["Position"] == "SF", "TOV"]) # Small Forward TOV range
range5 = max(df.loc[df["Position"] == "SG", "TOV"]) - min(df.loc[df["Position"] == "SF", "TOV"]) # Shooting Guard TOV range

std1 = df.loc[df["Position"] == "C", "TOV"].std()   # Center TOV std
std2 = df.loc[df["Position"] == "PF", "TOV"].std()  # Power Forward TOV std
std3 = df.loc[df["Position"] == "PG", "TOV"].std()  # Point Guard TOV std
std4 = df.loc[df["Position"] == "SF", "TOV"].std()  # Small Forward TOV std
std5 = df.loc[df["Position"] == "SG", "TOV"].std()  # Shooting Guard TOV std

var1 = df.loc[df["Position"] == "C", "TOV"].var()  # Center TOV variance
var2 = df.loc[df["Position"] == "PF", "TOV"].var() # Power Forward TOV variance
var3 = df.loc[df["Position"] == "PG", "TOV"].var() # Point Guard TOV variance
var4 = df.loc[df["Position"] == "SF", "TOV"].var() # Small Forward TOV variance
var5 = df.loc[df["Position"] == "SG", "TOV"].var() # Shooting Guard TOV variance

avg1 = df.loc[df["Position"] == "C", "TOV"].sum() / 91   # Center TOV avg
avg2 = df.loc[df["Position"] == "PF", "TOV"].sum() / 86  # Power Forward TOV avg
avg3 = df.loc[df["Position"] == "PG", "TOV"].sum() / 79  # Point Guard TOV avg
avg4 = df.loc[df["Position"] == "SF", "TOV"].sum() / 94  # Small Forward TOV avg
avg5 = df.loc[df["Position"] == "SG", "TOV"].sum() / 117  # Shooting Guard TOV avg


for position in positions:
    print(f"{Format.underline}\n{position} TOV\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["TOV"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} TOV is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["TOV"].max() if not subset.empty else "N/A"
            minVal = subset["TOV"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} TOV is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["TOV"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} TOV is {meanVal:.2f}")
        else:
            statVal = getattr(subset["TOV"], stat)()
            print(f"The {stat} value of the {position} TOV is {statVal:.2f}")
        print()

# Personal Fouls Per Game
print(Format.underline + "\nPersonal Fouls Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "PF"].mean()   # Center PF mean
mean2 = df.loc[df["Position"] == "PF", "PF"].mean()  # Power Forward PF mean
mean3 = df.loc[df["Position"] == "PG", "PF"].mean()  # Point Guard PF mean
mean4 = df.loc[df["Position"] == "SF", "PF"].mean()  # Small Forward PF mean
mean5 = df.loc[df["Position"] == "SG", "PF"].mean()  # Shooting Guard PF mean

mode1 = df.loc[df["Position"] == "C", "PF"].mode()   # Center PF mode
mode2 = df.loc[df["Position"] == "PF", "PF"].mode()  # Power Forward PF mode
mode3 = df.loc[df["Position"] == "PG", "PF"].mode()  # Point Guard PF mode
mode4 = df.loc[df["Position"] == "SF", "PF"].mode()  # Small Forward PF mode
mode5 = df.loc[df["Position"] == "SG", "PF"].mode()  # Shooting Guard PF mode

median1 = df.loc[df["Position"] == "C", "PF"].median()  # Center PF median
median2 = df.loc[df["Position"] == "PF", "PF"].median() # Power Forward PF median
median3 = df.loc[df["Position"] == "PG", "PF"].median() # Point Guard PF median
median4 = df.loc[df["Position"] == "SF", "PF"].median() # Small Forward PF median
median5 = df.loc[df["Position"] == "SG", "PF"].median() # Shooting Guard PF median

range1 = max(df.loc[df["Position"] == "C", "PF"]) - min(df.loc[df["Position"] == "C", "PF"])   # Center PF range
range2 = max(df.loc[df["Position"] == "PF", "PF"]) - min(df.loc[df["Position"] == "PF", "PF"]) # Power Forward PF range
range3 = max(df.loc[df["Position"] == "PG", "PF"]) - min(df.loc[df["Position"] == "PG", "PF"]) # Point Guard PF range
range4 = max(df.loc[df["Position"] == "SF", "PF"]) - min(df.loc[df["Position"] == "SF", "PF"]) # Small Forward PF range
range5 = max(df.loc[df["Position"] == "SG", "PF"]) - min(df.loc[df["Position"] == "SF", "PF"]) # Shooting Guard PF range

std1 = df.loc[df["Position"] == "C", "PF"].std()   # Center PF std
std2 = df.loc[df["Position"] == "PF", "PF"].std()  # Power Forward PF std
std3 = df.loc[df["Position"] == "PG", "PF"].std()  # Point Guard PF std
std4 = df.loc[df["Position"] == "SF", "PF"].std()  # Small Forward PF std
std5 = df.loc[df["Position"] == "SG", "PF"].std()  # Shooting Guard PF std

var1 = df.loc[df["Position"] == "C", "PF"].var()  # Center PF variance
var2 = df.loc[df["Position"] == "PF", "PF"].var() # Power Forward PF variance
var3 = df.loc[df["Position"] == "PG", "PF"].var() # Point Guard PF variance
var4 = df.loc[df["Position"] == "SF", "PF"].var() # Small Forward PF variance
var5 = df.loc[df["Position"] == "SG", "PF"].var() # Shooting Guard PF variance

avg1 = df.loc[df["Position"] == "C", "PF"].sum() / 91   # Center PF avg
avg2 = df.loc[df["Position"] == "PF", "PF"].sum() / 86  # Power Forward PF avg
avg3 = df.loc[df["Position"] == "PG", "PF"].sum() / 79  # Point Guard PF avg
avg4 = df.loc[df["Position"] == "SF", "PF"].sum() / 94  # Small Forward PF avg
avg5 = df.loc[df["Position"] == "SG", "PF"].sum() / 117  # Shooting Guard PF avg


for position in positions:
    print(f"{Format.underline}\n{position} PF\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["PF"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} PF is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["PF"].max() if not subset.empty else "N/A"
            minVal = subset["PF"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} PF is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["PF"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} PF is {meanVal:.2f}")
        else:
            statVal = getattr(subset["PF"], stat)()
            print(f"The {stat} value of the {position} PF is {statVal:.2f}")
        print()

# Points Per Game
print(Format.underline + "\nPoints Per Game\n" + Format.end)
mean1 = df.loc[df["Position"] == "C", "PTS"].mean()   # Center PTS mean
mean2 = df.loc[df["Position"] == "PF", "PTS"].mean()  # Power Forward PTS mean
mean3 = df.loc[df["Position"] == "PG", "PTS"].mean()  # Point Guard PTS mean
mean4 = df.loc[df["Position"] == "SF", "PTS"].mean()  # Small Forward PTS mean
mean5 = df.loc[df["Position"] == "SG", "PTS"].mean()  # Shooting Guard PTS mean

mode1 = df.loc[df["Position"] == "C", "PTS"].mode()   # Center PTS mode
mode2 = df.loc[df["Position"] == "PF", "PTS"].mode()  # Power Forward PTS mode
mode3 = df.loc[df["Position"] == "PG", "PTS"].mode()  # Point Guard PTS mode
mode4 = df.loc[df["Position"] == "SF", "PTS"].mode()  # Small Forward PTS mode
mode5 = df.loc[df["Position"] == "SG", "PTS"].mode()  # Shooting Guard PTS mode

median1 = df.loc[df["Position"] == "C", "PTS"].median()  # Center PTS median
median2 = df.loc[df["Position"] == "PF", "PTS"].median() # Power Forward PTS median
median3 = df.loc[df["Position"] == "PG", "PTS"].median() # Point Guard PTS median
median4 = df.loc[df["Position"] == "SF", "PTS"].median() # Small Forward PTS median
median5 = df.loc[df["Position"] == "SG", "PTS"].median() # Shooting Guard PTS median

range1 = max(df.loc[df["Position"] == "C", "PTS"]) - min(df.loc[df["Position"] == "C", "PTS"])   # Center PTS range
range2 = max(df.loc[df["Position"] == "PF", "PTS"]) - min(df.loc[df["Position"] == "PF", "PTS"]) # Power Forward PTS range
range3 = max(df.loc[df["Position"] == "PG", "PTS"]) - min(df.loc[df["Position"] == "PG", "PTS"]) # Point Guard PTS range
range4 = max(df.loc[df["Position"] == "SF", "PTS"]) - min(df.loc[df["Position"] == "SF", "PTS"]) # Small Forward PTS range
range5 = max(df.loc[df["Position"] == "SG", "PTS"]) - min(df.loc[df["Position"] == "SF", "PTS"]) # Shooting Guard PTS range

std1 = df.loc[df["Position"] == "C", "PTS"].std()   # Center PTS std
std2 = df.loc[df["Position"] == "PF", "PTS"].std()  # Power Forward PTS std
std3 = df.loc[df["Position"] == "PG", "PTS"].std()  # Point Guard PTS std
std4 = df.loc[df["Position"] == "SF", "PTS"].std()  # Small Forward PTS std
std5 = df.loc[df["Position"] == "SG", "PTS"].std()  # Shooting Guard PTS std

var1 = df.loc[df["Position"] == "C", "PTS"].var()  # Center PTS variance
var2 = df.loc[df["Position"] == "PF", "PTS"].var() # Power Forward PTS variance
var3 = df.loc[df["Position"] == "PG", "PTS"].var() # Point Guard PTS variance
var4 = df.loc[df["Position"] == "SF", "PTS"].var() # Small Forward PTS variance
var5 = df.loc[df["Position"] == "SG", "PTS"].var() # Shooting Guard PTS variance

avg1 = df.loc[df["Position"] == "C", "PTS"].sum() / 91   # Center PTS avg
avg2 = df.loc[df["Position"] == "PF", "PTS"].sum() / 86  # Power Forward PTS avg
avg3 = df.loc[df["Position"] == "PG", "PTS"].sum() / 79  # Point Guard PTS avg
avg4 = df.loc[df["Position"] == "SF", "PTS"].sum() / 94  # Small Forward PTS avg
avg5 = df.loc[df["Position"] == "SG", "PTS"].sum() / 117  # Shooting Guard PTS avg


for position in positions:
    print(f"{Format.underline}\n{position} PTS\n{Format.end}")
    subset = df[df["Position"] == position]
    
    for stat in statistics:
        if stat == "mode":
            modeVal = subset["PTS"].mode().iloc[0] if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} PTS is {modeVal:.2f}")
        elif stat == "range":
            maxVal = subset["PTS"].max() if not subset.empty else "N/A"
            minVal = subset["PTS"].min() if not subset.empty else "N/A"
            rangeVal = maxVal - minVal
            print(f"The {stat} value of the {position} PTS is {rangeVal:.2f}")
        elif stat == "mean":
            meanVal = subset["PTS"].mean() if not subset.empty else "N/A"
            print(f"The {stat} value of the {position} PTS is {meanVal:.2f}")
        else:
            statVal = getattr(subset["PTS"], stat)()
            print(f"The {stat} value of the {position} PTS is {statVal:.2f}")
        print()